from .models import UserTestAttempt
from apps.profiling.models import TraitVector


# ──────────────────────────────
# 🎯 TEST SCORING ENGINE (FINAL - STABLE)
# ──────────────────────────────
def calculate_test_scores(attempt_id):
    attempt = UserTestAttempt.objects.select_related('test').get(id=attempt_id)
    test = attempt.test

    answers = attempt.answers.select_related('selected_option', 'question')

    trait_scores = {}
    trait_weights = {}

    # 🔥 CONFIG BASED ON TEST TYPE
    NEGATIVE_MARKING = test.category == 'cognitive'
    TIME_BONUS = test.test_type == 'timed'
    PERSONALITY_MODE = test.category == 'personality'

    for ans in answers:

        if not ans.selected_option:
            continue

        q = ans.question
        option = ans.selected_option

        difficulty = q.difficulty_multiplier or 1.0

        # ============================
        # 🎯 BASE SCORE FROM OPTION
        # ============================
        for trait, value in option.scores.items():

            base_score = float(value)

            # 🧠 Personality → no difficulty bias
            if PERSONALITY_MODE:
                weighted_score = base_score
                weight = 1.0
            else:
                weighted_score = base_score * difficulty
                weight = difficulty

            # ❌ Negative marking (only cognitive)
            if NEGATIVE_MARKING and not option.is_correct:
                weighted_score = -0.25 * difficulty

            # ⏱️ Time bonus (safe & controlled)
            if TIME_BONUS and ans.time_taken_secs:
                if ans.time_taken_secs < 10:
                    weighted_score *= 1.05
                elif ans.time_taken_secs > 30:
                    weighted_score *= 0.95

            # 🔢 Aggregate
            trait_scores[trait] = trait_scores.get(trait, 0) + weighted_score
            trait_weights[trait] = trait_weights.get(trait, 0) + weight

    # ============================
    # 📊 NORMALIZATION (0 → 1)
    # ============================
    normalized = {}

    for t in trait_scores:
        score = trait_scores[t] / max(trait_weights[t], 1)

        # Clamp safely
        normalized[t] = max(0, min(score, 1))

    attempt.trait_scores = normalized
    attempt.save()

    # 🔥 Update global profile
    update_trait_vector(attempt.user)


# ──────────────────────────────
# 🧠 TRAIT VECTOR (AVERAGE MODEL - SAFE)
# ──────────────────────────────
def update_trait_vector(user):
    attempts = UserTestAttempt.objects.filter(user=user, status='completed')

    aggregate = {}
    count = {}

    for attempt in attempts:
        for trait, score in attempt.trait_scores.items():
            aggregate[trait] = aggregate.get(trait, 0) + float(score)
            count[trait] = count.get(trait, 0) + 1

    final_traits = {
        t: aggregate[t] / max(count[t], 1)   # ✅ safe division
        for t in aggregate
    }

    vector, _ = TraitVector.objects.get_or_create(user=user)

    for trait, value in final_traits.items():
        if hasattr(vector, trait):
            setattr(vector, trait, float(value))

    # Confidence based on number of tests
    vector.confidence_score = min(1.0, len(attempts) / 5)

    vector.save()


# ──────────────────────────────
# 🔥 PEAK MODEL (BEST PERFORMANCE)
# ──────────────────────────────
def sync_trait_vector(user):
    """
    Uses BEST score per trait (peak performance model)
    """
    vector, _ = TraitVector.objects.get_or_create(user=user)

    attempts = UserTestAttempt.objects.filter(user=user, status='completed')

    for attempt in attempts:
        for trait, score in attempt.trait_scores.items():
            if hasattr(vector, trait):
                current_val = getattr(vector, trait) or 0.0
                setattr(vector, trait, max(current_val, float(score)))

    categories_done = attempts.values('test__category').distinct().count()
    vector.confidence_score = min(categories_done * 0.2, 1.0)

    vector.save()


# ──────────────────────────────
# 🧩 USER SKILLS EXTRACTION
# ──────────────────────────────
def get_user_skills(user):
    attempts = UserTestAttempt.objects.filter(user=user, status='completed')

    skills = {}

    for att in attempts:
        for trait, score in att.trait_scores.items():
            skills[trait] = max(skills.get(trait, 0), float(score))

    return skills


# ──────────────────────────────
# 🚀 CAREER MATCHING ENGINE
# ──────────────────────────────
def get_top_career_matches(user, top_n=5):
    skills = get_user_skills(user)

    career_skills = {
        "Data Scientist": {
            "logical_reasoning": 0.9,
            "numerical_aptitude": 0.9,
            "attention_to_detail": 0.8
        },
        "UX Designer": {
            "creativity": 0.9,
            "empathy": 0.8,
            "communication": 0.7
        },
        "Software Engineer": {
            "logical_reasoning": 0.9,
            "problem_solving": 0.9,
            "attention_to_detail": 0.8
        },
        "Marketing Manager": {
            "communication": 0.9,
            "enterprising": 0.8,
            "creativity": 0.7
        },
    }

    match_scores = {}

    for career, req in career_skills.items():
        score = sum(
            min(skills.get(skill, 0) / val, 1)
            for skill, val in req.items()
        ) / len(req)

        match_scores[career] = score

    return sorted(match_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]


# ──────────────────────────────
# 📉 SKILL GAP ANALYSIS
# ──────────────────────────────
def calculate_skill_gaps(user):
    skills = get_user_skills(user)

    career_skills = {
        "Data Scientist": {
            "logical_reasoning": 0.9,
            "numerical_aptitude": 0.9
        },
        "UX Designer": {
            "creativity": 0.9,
            "empathy": 0.8
        },
    }

    gaps = {}

    for career, req in career_skills.items():
        gaps[career] = {
            skill: max(0, req_val - skills.get(skill, 0))
            for skill, req_val in req.items()
        }

    return gaps

def generate_personality_summary(traits):
    if not traits:
        return "Complete tests to unlock your personality insights."

    sorted_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)

    top_traits = [t[0].replace("_", " ").title() for t in sorted_traits[:3]]

    summary = f"""
You demonstrate strong {top_traits[0]}, supported by {top_traits[1]} and {top_traits[2]}.

This indicates a personality that is capable of handling complex situations with clarity, adaptability, and structured thinking.

You are likely to perform well in environments that require decision-making, collaboration, and problem-solving under uncertainty.
    """

    return summary.strip()

