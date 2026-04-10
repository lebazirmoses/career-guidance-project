from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import Test, UserTestAttempt, UserAnswer, Option
from .services import (
    calculate_test_scores,
    get_top_career_matches,
    calculate_skill_gaps
)


# ──────────────────────────────
# 📋 TEST LIST
# ──────────────────────────────
@login_required
def test_list(request):
    user = request.user
    profile = getattr(user, 'profile', None)

    tests = Test.objects.all()

    # 🔥 FILTER BASED ON USER LEVEL
    if profile:
        if profile.current_stage in ['school_low', 'school_high']:
            if profile.class_level:
                tests = tests.filter(
                    applicable_levels__icontains=str(profile.class_level)
                )
        else:
            tests = tests.filter(
                applicable_levels__icontains=profile.current_stage
            )

    tests = tests.order_by('order')

    # Map attempts
    attempts = UserTestAttempt.objects.filter(user=user)
    attempt_map = {a.test_id: a.status for a in attempts}

    for test in tests:
        test.user_status = attempt_map.get(test.id, 'not_started')

    return render(request, 'assessments/test_list.html', {
        'tests': tests
    })


# ──────────────────────────────
# 🧠 TAKE TEST
# ──────────────────────────────
@login_required
def take_test(request, slug):
    test = get_object_or_404(Test, slug=slug)

    attempt, created = UserTestAttempt.objects.get_or_create(
        user=request.user,
        test=test,
        defaults={
            'status': 'in_progress',
            'started_at': timezone.now()
        }
    )

    # 🚫 Prevent retake
    if attempt.status == 'completed':
        return redirect('assessments:test_results', slug=slug)

    questions = test.questions.filter(is_active=True).prefetch_related('options')

    if request.method == 'POST':

        answered_count = 0

        for q in questions:
            selected_option_id = request.POST.get(f'q_{q.id}')

            if selected_option_id:
                try:
                    option = Option.objects.get(id=selected_option_id, question=q)
                except Option.DoesNotExist:
                    continue

                UserAnswer.objects.update_or_create(
                    attempt=attempt,
                    question=q,
                    defaults={
                        'selected_option': option,
                        'answer_text': option.text,
                        'is_correct': option.is_correct
                    }
                )
                answered_count += 1

        # 🔥 VALIDATION: Ensure all questions answered
        if answered_count < questions.count():
            messages.error(request, "Please answer all questions before submitting.")
            return redirect('assessments:take_test', slug=slug)

        # ✅ Complete attempt
        attempt.status = 'completed'
        attempt.completed_at = timezone.now()
        attempt.save()

        # 🔥 CALCULATE SCORES
        calculate_test_scores(attempt.id)

        return redirect('assessments:test_results', slug=slug)

    return render(request, 'assessments/take_test.html', {
        'test': test,
        'questions': questions
    })


# ──────────────────────────────
# 📊 RESULTS (🔥 FINAL VERSION)
# ──────────────────────────────
@login_required
def test_results(request, slug):
    attempt = get_object_or_404(
        UserTestAttempt.objects.select_related('test'),
        user=request.user,
        test__slug=slug
    )

    # 🚫 Safety: Prevent accessing incomplete results
    if attempt.status != 'completed':
        messages.warning(request, "Complete the test to view results.")
        return redirect('assessments:take_test', slug=slug)

    # 🔥 Convert to percentages
    trait_percentages = {
        trait: round(float(score) * 100, 2)
        for trait, score in attempt.trait_scores.items()
    }

    # 🔥 Sort traits (highest first → better UX)
    trait_percentages = dict(
        sorted(trait_percentages.items(), key=lambda x: x[1], reverse=True)
    )

    # 🚀 Career recommendations
    careers = get_top_career_matches(request.user)

    # Convert career scores → %
    careers_percent = [
        (career, round(score * 100, 2))
        for career, score in careers
    ]

    # 📉 Skill gaps
    gaps = calculate_skill_gaps(request.user)

    return render(request, 'assessments/results.html', {
        'attempt': attempt,
        'traits_percent': trait_percentages,
        'careers': careers_percent,
        'gaps': gaps
    })
    
    
def start_next_test(request):
    user = request.user

    tests = Test.objects.order_by('order')

    completed = UserTestAttempt.objects.filter(
        user=user,
        status='completed'
    ).values_list('test_id', flat=True)

    next_test = tests.exclude(id__in=completed).first()

    if next_test:
        return redirect('assessments:take_test', slug=next_test.slug)

    return redirect('assessments:test_list')

