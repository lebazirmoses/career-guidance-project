import math
from .models import TraitVector, Career

def cosine_similarity(v1, v2):
    keys = set(v1.keys()) & set(v2.keys())
    if not keys: return 0
    dot = sum(v1[k] * v2[k] for k in keys)
    mag1 = math.sqrt(sum(v1[k]**2 for k in keys))
    mag2 = math.sqrt(sum(v2[k]**2 for k in keys))
    if mag1==0 or mag2==0: return 0
    return dot / (mag1*mag2)

def is_career_eligible(profile, career):
    name = career.name.lower()
    if "doctor" in name and not profile.has_biology: return False
    if "engineer" in name and not profile.has_maths: return False
    if "accountant" in name and not profile.has_commerce: return False
    return True

def calculate_gaps(user_vec, career_vec):
    gaps = []
    for key in career_vec:
        diff = career_vec[key] - user_vec.get(key, 0)
        if diff > 0.2: gaps.append(key)
    return sorted(gaps, key=lambda x: career_vec[x], reverse=True)

def get_recommendations(user, top_n=6):
    try: vector = TraitVector.objects.get(user=user)
    except TraitVector.DoesNotExist: return []

    profile = user.profile
    user_vec = vector.to_dict()
    results = []

    for career in Career.objects.all():
        if not is_career_eligible(profile, career): continue
        career_vec = career.get_vector()
        score = cosine_similarity(user_vec, career_vec)
        gaps = calculate_gaps(user_vec, career_vec)
        results.append({
            "career": career,
            "score": score,
            "match_percentage": round(score*100),
            "gaps": gaps[:3]
        })
    return sorted(results, key=lambda x: x["score"], reverse=True)[:top_n]

def generate_career_tree(user):
    top_career = get_recommendations(user, top_n=1)
    if not top_career: return {}

    profile = user.profile
    career = top_career[0]['career']

    tree = {
        "name": profile.current_stage or "Profile",
        "children": [
            {
                "name": f"Stream: {profile.stream or 'N/A'}",
                "children": [
                    {
                        "name": f"Degree: {profile.degree or 'N/A'}",
                        "children": [{"name": step} for step in career.roadmap_steps]
                    }
                ]
            }
        ]
    }
    return tree


# apps/profiling/services.py

import json
from django.conf import settings
from pathlib import Path

def load_profession_roadmap(profession_file="doctor.json"):
    """
    Loads the career roadmap JSON for a specific profession.
    """
    path = Path(settings.BASE_DIR) / "dashboard" / "career_paths" / profession_file
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def get_roadmap_for_profession(profession_name="Doctor"):
    """
    Returns roadmap details for a profession.
    Currently only matches Doctor/doctor.json.
    """
    # In future, can map profession_name -> json file dynamically
    profession_file = "doctor.json" if profession_name.lower() == "doctor" else None
    if not profession_file:
        return {"error": "Profession not found"}

    roadmap_data = load_profession_roadmap(profession_file)
    return roadmap_data