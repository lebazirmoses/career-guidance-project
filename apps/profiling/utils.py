# apps/profiling/utils.py

from apps.profiling.models import TraitVector


# ──────────────────────────────
# 📊 PROFILE COMPLETION
# ──────────────────────────────
def calculate_profile_completion(profile):
    """
    Calculates how complete the user profile is (0–100%)
    """

    fields = [
        getattr(profile, "current_stage", None),
        getattr(profile, "class_level", None),
        getattr(profile, "degree", None),
        getattr(profile, "specialization", None),
    ]

    filled = sum(1 for f in fields if f)
    total = len(fields)

    return int((filled / total) * 100) if total > 0 else 0


# ──────────────────────────────
# 🧠 EXTRACT USER TRAITS
# ──────────────────────────────
from apps.profiling.models import TraitVector


def extract_user_traits(user):
    try:
        vector = TraitVector.objects.get(user=user)
    except TraitVector.DoesNotExist:
        return {}, False, 0

    traits = {}

    for field in vector._meta.fields:
        field_name = field.name

        # 🚫 Skip non-trait fields
        if field_name in ['id', 'user', 'created_at', 'updated_at', 'confidence_score']:
            continue

        value = getattr(vector, field_name)

        # ✅ Only include numeric values
        if isinstance(value, (int, float)):
            traits[field_name] = float(value)

    # 🚀 Sort traits (best first)
    traits = dict(sorted(traits.items(), key=lambda x: x[1], reverse=True))

    has_traits = len(traits) > 0
    confidence = getattr(vector, 'confidence_score', 0)

    return traits, has_traits, confidence

# ──────────────────────────────
# 🌳 CAREER TREE GENERATION
# ──────────────────────────────
def generate_career_tree(user_profile):
    """
    Generate a tree:
    School → Stream → College → Degree → Career Path
    """

    # ⚠️ Lazy import to avoid circular dependency
    from apps.profiling.services import get_top_career

    careers = get_top_career(user_profile, top_n=1)

    if not careers:
        return {"name": "No Data", "children": []}

    top_career = careers[0]["career"]

    return {
        "name": getattr(user_profile, "current_stage", "School"),
        "children": [
            {
                "name": f"Stream: {getattr(user_profile, 'stream', 'General')}",
                "children": [
                    {
                        "name": "College Options",
                        "children": [
                            {
                                "name": "Recommended Path",
                                "children": [
                                    {"name": step}
                                    for step in getattr(top_career, "roadmap_steps", [])
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }