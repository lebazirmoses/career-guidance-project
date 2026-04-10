# apps/dashboard/utils.py
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from apps.dashboard.models import CareerNode

# PDF Rendering
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return result.getvalue()
    return None

# Career Tree Seeder
def seed_career_tree(nested_data, parent_node=None, current_stage="stream"):
    """
    Recursively parses a nested JSON dict and creates Django CareerNodes.
    """
    for key, value in nested_data.items():
        # Skip structural grouping keys
        if key in ["degrees", "specializations"]:
            seed_career_tree(value, parent_node, current_stage)
            continue

        # Create DB node
        node, created = CareerNode.objects.get_or_create(
            name=key,
            parent=parent_node,
            defaults={"stage": current_stage}
        )

        # Handle nested dictionaries
        if isinstance(value, dict):
            next_stage = {
                "stream": "subject_group",
                "subject_group": "degree",
                "degree": "specialization"
            }.get(current_stage, "sub_specialization")
            
            seed_career_tree(value, node, next_stage)

        # Handle leaf nodes (lists of careers)
        elif isinstance(value, list):
            for career_name in value:
                CareerNode.objects.get_or_create(
                    name=career_name,
                    parent=node,
                    defaults={"stage": "career"}
                )
                
# apps/dashboard/utils.py

from apps.assessments.services import get_top_career_matches


# ──────────────────────────────
# 🚀 AI DATA AGGREGATOR
# ──────────────────────────────
def get_ai_data(user, has_traits):
    """
    Returns:
    - career matches
    - roadmap text
    """

    if not has_traits:
        return [], "Complete assessments to unlock AI insights."

    matches = get_top_career_matches(user)

    ai_matches = []
    for career, score in matches:
        ai_matches.append({
            "career": {
                "name": career,
                "description": f"Recommended based on your strengths in {career} related skills."
            },
            "match_percentage": int(score * 100),
            "gaps": []
        })

    roadmap = generate_simple_roadmap(matches)

    return ai_matches, roadmap


# ──────────────────────────────
# 🧠 SIMPLE ROADMAP GENERATOR
# ──────────────────────────────
def generate_simple_roadmap(matches):
    if not matches:
        return "No roadmap available yet."

    top_career = matches[0][0]

    return f"""
Recommended Path → {top_career}

1. Build strong fundamentals
2. Take relevant degree/course
3. Work on real-world projects
4. Gain internships
5. Specialize and grow

Stay consistent — you're on the right track 🚀
"""