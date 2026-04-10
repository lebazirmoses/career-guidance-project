import json
import re
from django.core.cache import cache
from apps.profiling.ai_client import call_gemini

# =========================================================
# 🔹 SAFE JSON EXTRACTION
# =========================================================
def extract_json(text):
    if not text:
        return []

    match = re.search(r'\[.*\]', text, re.DOTALL)
    if not match:
        return []

    try:
        return json.loads(match.group(0))
    except Exception:
        return []

# =========================================================
# 🔹 CONTEXT BUILDER (SMART TRAITS)
# =========================================================
def build_context(user, node_name):
    traits = getattr(user, "trait_vector", None)
    trait_summary = ""
    trait_dict = {}

    if traits:
        trait_dict = traits.to_dict()
        top_traits = sorted(trait_dict.items(), key=lambda x: x[1], reverse=True)[:4]
        trait_summary = ", ".join([f"{k}:{round(v,2)}" for k, v in top_traits if v > 0])

    return trait_summary, trait_dict

# =========================================================
# 🔹 PROMPT ENGINE (MORE CONTROLLED)
# =========================================================
def build_prompt(node_name, trait_summary):
    return f"""
You are an expert AI Career Advisor for Indian students.

Current Node: {node_name}
User Traits: {trait_summary if trait_summary else "General"}

Think carefully:

1. Identify current stage (school / degree / specialization / job)
2. Suggest NEXT logical steps
3. Keep progression realistic

Rules:
- 10 to 12 options only
- Mix of degrees, specializations, careers
- Avoid repetition
- Keep names short and clean

Output ONLY JSON list.
"""

# =========================================================
# 🔥 TRAIT-BASED HEAT SCORING
# =========================================================
def compute_heat(node_name, traits):
    if not traits:
        return 0.3

    mapping = {
        "ai": "logic",
        "data": "logic",
        "engineering": "logic",
        "design": "creativity",
        "art": "creativity",
        "psychology": "social",
        "management": "social",
        "law": "verbal",
        "teaching": "verbal",
    }

    score = 0
    name = node_name.lower()

    for keyword, trait in mapping.items():
        if keyword in name:
            score += traits.get(trait, 0)

    return round(min(score, 1), 2)

# =========================================================
# 🔥 RANKING ENGINE
# =========================================================
def rank_options(options, traits):
    ranked = []

    for opt in options:
        heat = compute_heat(opt, traits)

        # Bonus signals
        if "ai" in opt.lower() and traits.get("logic", 0) > 0.6:
            heat += 0.2
        if "design" in opt.lower() and traits.get("creativity", 0) > 0.6:
            heat += 0.2

        ranked.append((heat, opt))

    ranked.sort(reverse=True)
    return [opt for _, opt in ranked]

# =========================================================
# 🔹 OFFLINE TREE DATA
# =========================================================
OFFLINE_TREE = {
    "root_science": ["PCM", "PCB", "PCMB", "Biotech", "Environmental Science"],
    "root_science_0": ["B.Sc Physics", "B.Sc Chemistry", "B.Sc Maths", "B.Tech CSE", "MBBS"],
    "root_science_0_0": ["M.Sc Physics", "M.Tech AI", "B.Ed Physics", "Internship Physics Lab", "Research Assistant"],
    "root_arts": ["BA Psychology", "Journalism", "Law", "Design", "Civil Services"],
    "root_commerce": ["B.Com", "BBA", "CA", "CS", "Finance"],
    "root_medical": ["MBBS", "BDS", "Nursing", "Physiotherapy", "Pharmacy"],
    "root_vocational": ["Diploma IT", "Diploma Mech", "ITI Electrician", "ITI Fitter", "HVAC"],
}

# =========================================================
# 🔹 SMART FALLBACK ENGINE
# =========================================================
def smart_fallback(node_name):
    node = node_name.lower()

    mapping = {
        "science": ["PCM", "PCB", "PCMB", "Biotech", "Environmental Science", "B.Tech", "MBBS"],
        "commerce": ["B.Com", "BBA", "CA", "CS", "CMA", "Finance", "Investment Banking"],
        "arts": ["BA Psychology", "Journalism", "Law", "Design", "Civil Services"],
        "engineering": ["Computer Science", "Mechanical", "Civil", "AI & ML", "Cyber Security"],
        "medical": ["Surgery", "Radiology", "Cardiology", "Neurology", "Dermatology"],
        "b.tech": ["CSE", "AI & ML", "Data Science", "Cloud", "Cyber Security", "Robotics"]
    }

    for key in mapping:
        if key in node:
            return mapping[key]

    return [
        "Higher Studies", "Certification", "Internship",
        "Freelancing", "Startup", "Government Jobs",
        "Private Jobs", "Research", "Specialization"
    ]

# =========================================================
# 🔥 MAIN ENGINE (ROBUST + GUARANTEED 5+ STEPS)
# =========================================================
def generate_next_steps(user, node_name):
    cache_key = f"ai_steps_v4_{node_name.lower()}_{user.id if user.is_authenticated else 'anon'}"
    cached = cache.get(cache_key)
    if cached:
        return cached

    trait_summary, trait_dict = build_context(user, node_name)
    prompt = build_prompt(node_name, trait_summary)

    try:
        # Call AI only if quota likely exists
        result = call_gemini(prompt)
        options = extract_json(result)

        # Clean and dedupe
        options = [str(o).strip() for o in options if isinstance(o, str) and len(o.strip()) > 2]
        options = list(dict.fromkeys(options))

        # If AI gives weak output, fallback
        if len(options) < 5:
            raise Exception("Weak AI output")

        # Rank using traits
        ranked_options = rank_options(options, trait_dict)
        final_options = ranked_options[:12]

    except Exception:
        # On quota failure or AI error, fallback
        final_options = smart_fallback(node_name)

    # Ensure minimum 5 options
    if len(final_options) < 5:
        fallback_extra = smart_fallback(node_name)
        final_options = list(dict.fromkeys(final_options + fallback_extra))[:12]

    cache.set(cache_key, final_options, timeout=3600)
    return final_options