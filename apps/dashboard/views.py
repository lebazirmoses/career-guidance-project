from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from django.core.cache import cache

from apps.assessments.models import UserTestAttempt, Test
from apps.profiling.services import get_recommendations
from apps.profiling.ai_client import generate_career_roadmap

from .models import CareerNode, Career
from .utils import render_to_pdf


# =========================================================
# 🔹 PROFILE COMPLETION ENGINE
# =========================================================
def calculate_profile_completion(profile):
    if not profile:
        return 0

    weights = {
        "current_stage": 0.15,
        "class_level": 0.10,
        "stream": 0.10,
        "subjects": 0.10,
        "interests": 0.10,
        "self_rated_skills": 0.15,
        "degree": 0.10,
        "specialization": 0.05,
        "institution": 0.05,
        "score": 0.10,
    }

    score = sum(
        weight for field, weight in weights.items()
        if getattr(profile, field, None)
    )

    return int(score * 100)


# =========================================================
# 🔹 TRAIT ENGINE (SAFE + NORMALIZED)
# =========================================================
def extract_user_traits(user):
    if not hasattr(user, 'trait_vector'):
        return {}, False, 0

    vector = user.trait_vector

    traits = {
        k: float(v)
        for k, v in vector.to_dict().items()
        if isinstance(v, (int, float)) and v > 0
    }

    confidence = getattr(vector, 'confidence_score', 0)

    return traits, bool(traits), confidence


# =========================================================
# 🔹 AI ENGINE (OPTIMIZED + FAULT-TOLERANT)
# =========================================================
def get_ai_data(user, has_traits):
    if not has_traits:
        return [], None

    cache_key = f"ai_data_{user.id}"
    cached = cache.get(cache_key)

    if cached:
        return cached

    try:
        recommendations = get_recommendations(user)

        if not recommendations:
            return [], None

        best_match = recommendations[0]

        try:
            roadmap = generate_career_roadmap(user, best_match)
        except Exception:
            roadmap = "⚠️ AI roadmap temporarily unavailable."

        cache.set(cache_key, (recommendations, roadmap), timeout=300)

        return recommendations, roadmap

    except Exception:
        return [], None


# =========================================================
# 🔹 CTA ENGINE
# =========================================================
def get_next_action(profile_completion, has_traits):
    if profile_completion < 60:
        return {'title': 'Complete Your Profile', 'link': 'onboarding:start'}

    if not has_traits:
        return {'title': 'Take Assessments', 'link': 'assessments:test_list'}

    return {'title': 'Explore Careers', 'link': 'dashboard:home'}


# =========================================================
# 🔹 DASHBOARD (CORE INTELLIGENCE HUB)
# =========================================================
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.assessments.models import Test, UserTestAttempt
from apps.profiling.utils import calculate_profile_completion, extract_user_traits
from apps.dashboard.utils import get_ai_data

from apps.assessments.services import generate_personality_summary

@login_required
def dashboard_home(request):
    user = request.user

    # 🚨 PROFILE CHECK
    if not hasattr(user, 'profile'):
        return redirect('onboarding:start')

    profile = user.profile
    profile_completion = calculate_profile_completion(profile)

    # 🚨 GATING
    if profile_completion < 50:
        return redirect('dashboard:profiling_hub')

    # 📊 TEST STATS
    completed_tests_count = UserTestAttempt.objects.filter(
        user=user,
        status='completed'
    ).count()

    total_tests = Test.objects.count()

    # 🧠 TRAITS + AI
    traits, has_traits, confidence = extract_user_traits(user)
    ai_matches, roadmap = get_ai_data(user, has_traits)
    # 🧠 AI Personality Summary
    ai_summary = generate_personality_summary(traits) if has_traits else ""

    # 🔥 STEP 2 — ADD HERE
    ai_summary = ""
    if has_traits:
        try:
            ai_summary = generate_personality_summary(traits)
        except Exception:
            ai_summary = "AI summary unavailable."

    # 🎯 NEXT ACTION
    if completed_tests_count == 0:
        next_action = {
            "title": "🚀 Start Your First Assessment",
            "link": "assessments:test_list"
        }

    elif completed_tests_count < total_tests:
        next_action = {
            "title": "🔥 Continue Your Assessments",
            "link": "assessments:test_list"
        }

    elif not has_traits:
        next_action = {
            "title": "🧠 Generate Insights",
            "link": "assessments:test_list"
        }

    else:
        next_action = {
            "title": "🌐 Explore Career Intelligence",
            "link": "dashboard:career_roadmap"
        }

    context = {
        'completed_tests_count': completed_tests_count,
        'total_tests': total_tests,
        'traits': traits,
        'has_traits': has_traits,
        'confidence': confidence,
        'profile_completion': profile_completion,
        'onboarding_percent': profile_completion,
        'ai_matches': ai_matches,
        'gemini_roadmap': roadmap,
        'next_action': next_action,

        # 🔥 ADD THIS
        'ai_summary': ai_summary,
    }

    return render(request, 'dashboard/home.html', context)

# =========================================================
# 🔹 PROFILING HUB (FIXED)
# =========================================================
@login_required
def profiling_hub(request):
    user = request.user
    profile = getattr(user, 'profile', None)

    profile_completion = calculate_profile_completion(profile)
    traits, has_traits, confidence = extract_user_traits(user)

    onboarding_url = 'onboarding:start' if profile_completion == 0 else 'onboarding:stage'

    return render(request, "dashboard/profiling_hub.html", {
        "profile_completion": profile_completion,
        "has_traits": has_traits,
        "confidence": confidence,
        "onboarding_url": onboarding_url,
    })


# =========================================================
# 🔹 TREE BUILDER (OPTIMIZED RECURSIVE)
# =========================================================
# =========================================================
# 🔹 TREE BUILDER (ZERO N+1 + DEPTH SAFE)
# =========================================================
def build_tree_cached(node, children_map, depth=0, max_depth=6):
    if depth > max_depth:
        return None

    children = [
        build_tree_cached(child, children_map, depth + 1, max_depth)
        for child in children_map.get(node.id, [])
    ]

    return {
        "id": node.id,
        "name": node.name,
        "stage": node.stage,
        "children": [c for c in children if c]
    }


# =========================================================
# 🔹 CAREER TREE VIEW (HIGH PERFORMANCE)
# =========================================================
def career_tree_view(request):
    cache_key = "career_tree_full_v2"
    tree = cache.get(cache_key)

    if not tree:
        nodes = CareerNode.objects.all()

        # Build parent-child map (⚡ no DB hits later)
        children_map = {}
        root_nodes = []

        for node in nodes:
            if node.parent_id:
                children_map.setdefault(node.parent_id, []).append(node)
            else:
                root_nodes.append(node)

        tree = {
            "name": "Career Paths",
            "children": [
                build_tree_cached(node, children_map)
                for node in root_nodes
            ]
        }

        cache.set(cache_key, tree, timeout=900)

    # 🎯 PERSONALIZATION
    recommended_names = []

    if request.user.is_authenticated:
        traits, has_traits, _ = extract_user_traits(request.user)

        if has_traits:
            recs = get_recommendations(request.user)
            recommended_names = [r.career.name for r in recs[:5]]

    return render(request, 'dashboard/career_tree.html', {
        'tree_data': tree,
        'recommended': recommended_names
    })

# =========================================================
# 🔹 CAREER DETAILS API (ADVANCED)
# =========================================================
@require_GET
def career_details_api(request):
    name = request.GET.get("name")

    if not name:
        return JsonResponse({"error": "Missing name"}, status=400)

    career = Career.objects.filter(name=name).first()

    traits, _, _ = extract_user_traits(request.user)

    if not career:
        return JsonResponse({
            "name": name,
            "description": "Explore further to find specific career paths.",
            "match_score": 0,
            "gaps": [],
            "strengths": [],
            "ai_path": ""
        })

    match_score = calculate_match_score(traits, career)
    gaps, strengths = analyze_skill_gap(traits, career)

    ai_path = ""
    try:
        ai_path = generate_career_roadmap(request.user, career)
    except:
        ai_path = "AI roadmap unavailable."

    return JsonResponse({
        "name": career.name,
        "description": career.description,
        "match_score": match_score,
        "gaps": gaps,
        "strengths": strengths,
        "ai_path": ai_path,
    })
    
# =========================================================
# 🔹 FUTURE PATH SIMULATOR (WOW FEATURE)
# =========================================================
@require_GET
def simulate_career_path(request):
    interest = request.GET.get("interest", "")
    current_stage = request.GET.get("stage", "school")

    # Simple rule-based simulation (can be replaced with AI later)
    if "ai" in interest.lower():
        path = [
            "10th → Science",
            "12th → PCM",
            "B.Tech → CSE",
            "Specialization → AI/ML",
            "Career → Machine Learning Engineer"
        ]
    else:
        path = ["Explore multiple streams based on your interests"]

    return JsonResponse({
        "input": {
            "interest": interest,
            "stage": current_stage
        },
        "predicted_path": path
    })


# =========================================================
# 🔹 PDF EXPORT
# =========================================================
@login_required
def export_career_report(request):
    user = request.user
    traits, has_traits, _ = extract_user_traits(user)

    ai_matches = []
    best_match = None
    roadmap = ""

    if has_traits:
        ai_matches = get_recommendations(user)
        best_match = ai_matches[0] if ai_matches else None

        if best_match:
            try:
                roadmap = generate_career_roadmap(user, best_match)
            except Exception:
                roadmap = "⚠️ Roadmap unavailable."

    pdf = render_to_pdf('dashboard/pdf_report.html', {
        'user': user,
        'traits': traits,
        'best_match': best_match,
        'roadmap': roadmap
    })

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={user.full_name}_Career_Report.pdf'
        return response

    return HttpResponse("Error generating PDF", status=400)


# =========================================================
# 🔹 FETCH CHILDREN (CORE DYNAMIC ENGINE)
# =========================================================

from .ai_tree import generate_next_steps
from django.db.models import Count
from .ai_tree import generate_next_steps


# 🔹 Static related expansion (VERY IMPORTANT)
RELATED_MAP = {
    "Science": ["PCM", "PCB", "PCMB", "Biotech", "Environmental Science"],
    "PCM": ["Engineering", "Architecture", "Defence", "Pure Sciences"],
    "Computer Science": [
        "Artificial Intelligence",
        "Data Science",
        "Cybersecurity",
        "Cloud Computing",
        "Web Development",
        "Game Development",
        "Blockchain",
        "DevOps",
        "Robotics"
    ],
}

from django.db.models import Q
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.core.cache import cache

from .models import CareerNode
from .ai_tree import generate_next_steps


MAX_AI_DEPTH = 6
MIN_CHILDREN = 8


def get_related_nodes(parent_node):
    """
    🔹 Smart DB expansion (VERY IMPORTANT)
    Finds nodes with similar stage OR name similarity
    """

    return CareerNode.objects.filter(
        Q(stage=parent_node.stage) |
        Q(name__icontains=parent_node.name[:4])
    ).exclude(parent=parent_node)[:10]

# =========================================================
# 🔥 SMART CHILD FETCH (TREE SAFE + CONTROLLED)
# =========================================================
# =========================================================
# 🔥 SMART CHILD FETCH (TREE SAFE + CONTROLLED)
# =========================================================
@require_GET
def get_children_api(request):
    parent_id = request.GET.get("parent_id")
    depth = int(request.GET.get("depth", 0))

    traits, has_traits, _ = extract_user_traits(request.user)

    cache_key = f"children_v6_{parent_id}_{depth}_{request.user.id if request.user.is_authenticated else 'anon'}"
    cached = cache.get(cache_key)
    if cached:
        return JsonResponse(cached)

    # =========================================
    # 🌱 ROOT LEVEL
    # =========================================
    if not parent_id:
        nodes = [
            {"id": "root_science", "name": "Science", "stage": "stream"},
            {"id": "root_commerce", "name": "Commerce", "stage": "stream"},
            {"id": "root_arts", "name": "Arts", "stage": "stream"},
            {"id": "root_vocational", "name": "Vocational", "stage": "stream"},
        ]

        return JsonResponse({"nodes": nodes})

    # =========================================
    # 🌿 ROOT EXPANSION (STATIC BASE)
    # =========================================
    ROOT_MAP = {
        "root_science": ["PCM", "PCB", "PCMB"],
        "root_commerce": ["Accounting", "Business", "Economics"],
        "root_arts": ["Psychology", "History", "Sociology"],
        "root_vocational": ["ITI", "Design", "Hotel Management"],
    }

    if parent_id in ROOT_MAP:
        nodes = [
            {
                "id": f"{parent_id}_{i}",
                "name": name,
                "stage": "subject_group",
                "heat": 0.5
            }
            for i, name in enumerate(ROOT_MAP[parent_id])
        ]
        return JsonResponse({"nodes": nodes})

    # =========================================
    # 🌳 GET PARENT NAME
    # =========================================
    parent_name = request.GET.get("parent_name")

    if not parent_name:
        # fallback (important fix)
        parent_name = parent_id.split("_")[-1]

    # =========================================
    # 🤖 AI EXPANSION (CORE ENGINE)
    # =========================================
    ai_nodes = []
    try:
        ai_options = generate_next_steps(request.user, parent_name)

        for i, opt in enumerate(ai_options[:10]):
            ai_nodes.append({
                "id": f"ai_{parent_id}_{i}",
                "name": opt,
                "stage": "dynamic",
                "heat": 0
            })

    except Exception:
        ai_nodes = []

    # =========================================
    # 🔥 FALLBACK (ALWAYS RETURNS SOMETHING)
    # =========================================
    if not ai_nodes:
        fallback = [
            "B.Tech",
            "B.Sc",
            "BCA",
            "Engineering",
            "Medicine",
            "Research",
            "Data Science",
            "AI Engineer"
        ]

        ai_nodes = [
            {
                "id": f"fallback_{i}",
                "name": f,
                "stage": "fallback",
                "heat": 0.4
            }
            for i, f in enumerate(fallback)
        ]

    # =========================================
    # 🎯 PERSONALIZATION (HEATMAP)
    # =========================================
    if has_traits:
        for node in ai_nodes:
            score = 0
            for trait, val in traits.items():
                score += val * 0.5  # simple weighting
            node["heat"] = min(1, score)

        ai_nodes = sorted(ai_nodes, key=lambda x: x["heat"], reverse=True)

    # =========================================
    # 🧠 AI SUGGESTION (NEXT BEST CLICK)
    # =========================================
    suggestion = ai_nodes[0]["name"] if ai_nodes else None

    response = {
        "nodes": ai_nodes[:12],
        "suggested": suggestion,
        "depth": depth
    }

    cache.set(cache_key, response, timeout=300)

    return JsonResponse(response)

# =========================================================
# 🔥 MATCH SCORE ENGINE
# =========================================================
def calculate_match_score(user_traits, career):
    if not user_traits or not career:
        return 0

    score = (
        user_traits.get("logic", 0) * career.required_logic +
        user_traits.get("creativity", 0) * career.required_creativity +
        user_traits.get("social", 0) * career.required_social +
        user_traits.get("verbal", 0) * career.required_verbal
    )

    return int(score * 100)


# =========================================================
# 🔥 SKILL GAP ANALYZER
# =========================================================
def analyze_skill_gap(user_traits, career):
    gaps = []
    strengths = []

    mapping = {
        "logic": career.required_logic,
        "creativity": career.required_creativity,
        "social": career.required_social,
        "verbal": career.required_verbal,
    }

    for trait, required in mapping.items():
        user_val = user_traits.get(trait, 0)

        if user_val < required:
            gaps.append(trait)
        else:
            strengths.append(trait)

    return gaps, strengths


# =========================================================
# 🔥 TRAIT-BASED RANKING
# =========================================================
def rank_nodes_by_traits(nodes, user_traits):
    if not user_traits:
        return nodes

    scored = []

    for node in nodes:
        score = 0

        for trait, value in user_traits.items():
            score += value * node.required_skills.get(trait, 0)

        scored.append((score, node))

    return [n for _, n in sorted(scored, reverse=True)]


import json
import logging
import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import google.generativeai as genai

# =========================================================
# 🔹 LOGGER SETUP
# =========================================================
logger = logging.getLogger(__name__)

# =========================================================
# 🔹 HELPER: Format history for Gemini
# =========================================================
def format_history(raw_history):
    """
    Converts frontend history [{role, content}] to Gemini format.
    """
    gemini_history = []
    for msg in raw_history:
        role = 'model' if msg.get('role') == 'assistant' else 'user'
        gemini_history.append({
            "role": role,
            "parts": [msg.get('content', '')]
        })
    return gemini_history

# =========================================================
# 🔹 HELPER: Initialize Gemini chat model
# =========================================================
def get_chat_model():
    api_key = getattr(settings, "GEMINI_API_KEY", None)
    if not api_key:
        logger.error("GEMINI_API_KEY is missing in settings!")
        return None
    try:
        # Configure the SDK once
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            model_name="models/gemini-3-flash-preview",  # Latest valid model
            generation_config={
                "temperature": 0.7,          # Encouraging + creative responses
                "max_output_tokens": 800,     # Limit response length
            },
            system_instruction=(
                "You are an expert Career Guidance AI for Indian students and professionals. "
                "Provide clear, structured roadmaps, skill recommendations, and career advice. "
                "Focus on Indian education streams (PCM, PCB, Commerce), degrees (B.Tech, MBBS, etc.), "
                "internships, and job market insights. "
                "If the user asks non-career questions, politely redirect them."
            )
        )
        logger.info("Gemini chat model initialized successfully.")
        return model
    except Exception as e:
        logger.critical(f"Failed to initialize Gemini chat model: {e}", exc_info=True)
        return None

# =========================================================
# 🔹 CHAT ENDPOINT
# =========================================================
@csrf_exempt
def career_chat(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed. Use POST."}, status=405)

    chat_model = get_chat_model()
    if not chat_model:
        return JsonResponse({
            "error": "AI model is unavailable. Check GEMINI_API_KEY in settings."
        }, status=503)

    try:
        data = json.loads(request.body)
        question = data.get("question", "").strip()
        raw_history = data.get("history", [])

        if not question:
            return JsonResponse({"error": "Question cannot be empty."}, status=400)

        gemini_history = format_history(raw_history)
        max_retries = 2

        for attempt in range(max_retries + 1):
            try:
                # Start chat session with history
                chat_session = chat_model.start_chat(history=gemini_history)
                response = chat_session.send_message(question)
                answer_text = response.text.strip()

                if not answer_text:
                    answer_text = (
                        "Hmm, I need more details to guide you. "
                        "Could you rephrase your question?"
                    )

                return JsonResponse({
                    "answer": answer_text,
                    "role": "assistant"
                }, status=200)

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries:
                    time.sleep(0.5)
                else:
                    raise e

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)
    except Exception as e:
        logger.error(f"🔥 Career Chat Error: {str(e)}", exc_info=True)
        return JsonResponse({
            "error": "AI is temporarily unavailable. Please try again shortly."
        }, status=503)
        
        
#=====================================
# 
#=====================================
        
@login_required
def assessments_view(request):
    # your logic here
    return render(request, "dashboard/home.html")
        

@login_required
def career_dashboard(request):
    """
    Renders the AI Career Guidance dashboard page.
    """
    return render(request, "ai_dashboard.html")


#=================================
# ROADMAP
#=================================


# apps/dashboard/views.py
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

# Map professions to their JSON filenames (can be dynamic from static/data folder)
DATA_FOLDER = Path(settings.BASE_DIR) / "static" / "data"

def load_profession_roadmap(file_name):
    path = DATA_FOLDER / file_name
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

@login_required
def career_roadmap_api(request):
    """
    Returns the roadmap JSON for a selected profession.
    Expects `?profession=<filename>` from dropdown.
    """
    profession_file = request.GET.get("profession", "").strip()
    if not profession_file:
        return JsonResponse({"error": "No profession selected"}, status=400)

    data = load_profession_roadmap(profession_file)
    if not data:
        return JsonResponse({"error": f"Roadmap not found for {profession_file}"}, status=404)

    return JsonResponse(data)

@login_required
def career_roadmap_page(request):
    """
    Renders the Career Roadmap Explorer page with dropdown list of all professions.
    """
    profession_files = []

    if DATA_FOLDER.exists():
        for f in DATA_FOLDER.glob("*.json"):
            profession_files.append({
                "name": f.stem.replace("_", " ").title(),  # Display name
                "file": f.name  # actual file for API
            })

    context = {"profession_files": profession_files}
    return render(request, "dashboard/career_roadmap.html", context)


@login_required
def get_roadmap_api(request):
    """
    API to return roadmap JSON for a profession
    """
    profession_name = request.GET.get("profession", "").lower()
    if not profession_name:
        return JsonResponse({"error": "No profession selected"}, status=400)

    # Map profession name to JSON file
    json_file = f"{profession_name}.json"
    roadmap = load_profession_roadmap(json_file)
    
    if not roadmap:
        return JsonResponse({"error": "Roadmap not found"}, status=404)
    
    return JsonResponse(roadmap)

# apps/dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ai_dashboard(request):
    user = request.user
    
    # Example context for your template
    context = {
        'user': user,
        'onboarding_percent': 80,
        'completed_tests_count': 3,
        'total_tests': 5,
        'has_traits': True,
        'traits': {'Logic': 0.8, 'Creativity': 0.6, 'Communication': 0.9},
        'ai_matches': [
            {'career': {'name': 'Data Scientist', 'description': 'Analyze data...'}, 'match_percentage': 95, 'gaps': ['Python', 'Statistics']},
            {'career': {'name': 'AI Engineer', 'description': 'Build AI models...'}, 'match_percentage': 88, 'gaps': ['Deep Learning']}
        ],
        'gemini_roadmap': 'Based on your traits, we suggest...',
        'next_action': {'title': 'Complete Python Module', 'link': 'dashboard:home'},
    }
    return render(request, 'dashboard/ai_dashboard.html', context)\
        

@login_required
def chatbot_page(request):
    return render(request, "dashboard/chatbot.html")