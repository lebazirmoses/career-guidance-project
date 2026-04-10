import json
import logging
from django.conf import settings
from django.core.cache import cache

from google import genai
from google.genai.types import GenerateContentConfig

logger = logging.getLogger(__name__)

# =========================================================
# 🔹 INIT (NEW GEMINI SDK)
# =========================================================
client = genai.Client(api_key=settings.GEMINI_API_KEY)

FAST_MODEL = "gemini-3.1-flash-lite-preview"
DEEP_MODEL = "gemini-2.5-pro"


# =========================================================
# 🔹 CORE GEMINI CALL (ROBUST + RETRY + FALLBACK)
# =========================================================
def call_gemini(prompt, temperature=0.7, max_tokens=800, json_mode=False):

    cache_key = f"gemini_{hash(prompt)}_{temperature}_{json_mode}"
    cached = cache.get(cache_key)

    if cached:
        return cached

    try:
        config = GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
            response_mime_type="application/json" if json_mode else "text/plain"
        )

        # 🔥 PRIMARY (FAST MODEL)
        response = client.models.generate_content(
            model=FAST_MODEL,
            contents=prompt,
            config=config
        )

        text = response.text if response and response.text else ""

        # 🔥 FALLBACK TO PRO IF EMPTY
        if not text:
            response = client.models.generate_content(
                model=DEEP_MODEL,
                contents=prompt,
                config=config
            )
            text = response.text if response and response.text else ""

        # 🔥 JSON PARSE (SAFE)
        if json_mode and text:
            try:
                text = json.loads(text)
            except Exception:
                logger.warning("JSON parse failed, returning raw text")

        cache.set(cache_key, text, timeout=3600)

        return text

    except Exception as e:
        logger.error(f"GEMINI ERROR: {e}")
        return {} if json_mode else ""


# =========================================================
# 🔹 CAREER ROADMAP (STRUCTURED + SMART)
# =========================================================
def generate_career_roadmap(user, match_data):

    profile = getattr(user, "profile", None)

    career_obj = match_data.get("career") if isinstance(match_data, dict) else None
    career_name = career_obj.name if career_obj else str(match_data)

    cache_key = f"roadmap_{user.id}_{career_name}"
    cached = cache.get(cache_key)

    if cached:
        return cached

    try:
        academic = profile.get_academic_profile() if profile else {}

        prompt = f"""
You are an expert Indian Career Advisor.

Return ONLY valid JSON.

STUDENT PROFILE:
Stream: {academic.get('stream')}
Strong Subjects: {academic.get('strong_subjects')}
Weak Subjects: {academic.get('weak_subjects')}
Score: {academic.get('percentage')}

CAREER:
{career_name}

OUTPUT FORMAT:
{{
  "title": "Career Name",
  "pathway": ["10th → ...", "12th → ...", "Degree → ..."],
  "skills": ["Skill 1", "Skill 2"],
  "projects": ["Project 1", "Project 2"],
  "timeline": ["Month 1", "Month 2"],
  "tips": ["Tip 1", "Tip 2"]
}}
"""

        data = call_gemini(prompt, json_mode=True)

        if not data:
            return "⚠️ AI roadmap unavailable."

        cache.set(cache_key, data, timeout=86400)

        return data

    except Exception as e:
        logger.error(f"ROADMAP ERROR: {e}")
        return "AI roadmap unavailable."


# =========================================================
# 🔹 AI NEXT STEP GENERATOR (TREE EXPANSION)
# =========================================================
def generate_next_steps(user, node_name):

    cache_key = f"ai_steps_{node_name}"
    cached = cache.get(cache_key)

    if cached:
        return cached

    try:
        prompt = f"""
You are a career guidance AI.

Given this node:
"{node_name}"

Generate 10 logical next career/education steps.

RULES:
- Short names only
- No explanations
- No duplicates
- Relevant to Indian education system

Return ONLY JSON array.

Example:
["B.Tech", "B.Sc", "Diploma"]
"""

        data = call_gemini(prompt, json_mode=True)

        if not isinstance(data, list):
            return []

        cache.set(cache_key, data, timeout=43200)

        return data

    except Exception as e:
        logger.error(f"AI TREE ERROR: {e}")
        return []


# =========================================================
# 🔹 AI CAREER EXPLANATION (FOR MODAL UI)
# =========================================================
def explain_career(career_name):

    cache_key = f"career_explain_{career_name}"
    cached = cache.get(cache_key)

    if cached:
        return cached

    try:
        prompt = f"""
Explain this career in a simple and engaging way:

{career_name}

FORMAT:
- What they do
- Required skills
- Salary range in India
- Future scope
"""

        text = call_gemini(prompt)

        cache.set(cache_key, text, timeout=86400)

        return text

    except Exception as e:
        logger.error(f"EXPLAIN ERROR: {e}")
        return "No details available."


# =========================================================
# 🔹 SKILL SUGGESTION ENGINE
# =========================================================
def suggest_skills(career_name):

    cache_key = f"skills_{career_name}"
    cached = cache.get(cache_key)

    if cached:
        return cached

    try:
        prompt = f"""
List top 8 skills required for:

{career_name}

Return JSON array.
"""

        skills = call_gemini(prompt, json_mode=True)

        if not isinstance(skills, list):
            return []

        cache.set(cache_key, skills, timeout=86400)

        return skills

    except Exception as e:
        logger.error(f"SKILL ERROR: {e}")
        return []