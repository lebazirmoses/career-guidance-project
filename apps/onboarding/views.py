from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.profiling.models import UserProfile
from apps.profiling.forms import (
    StageSelectionForm,
    SchoolLowForm,
    SchoolHighForm,
    UGForm,
    CommonForm
)


# ─────────────────────────────────────────────
# STEP 1 → SELECT STAGE
# ─────────────────────────────────────────────
@login_required
def onboarding_start(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = StageSelectionForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)

            # 🔥 Safety: ensure stage exists
            if not profile.current_stage:
                form.add_error(None, "Please select your current stage.")
            else:
                profile.save()
                return redirect('onboarding:stage')
    else:
        form = StageSelectionForm(instance=profile)

    return render(request, "onboarding/start.html", {
        "form": form,
        "percent": 20
    })


# ─────────────────────────────────────────────
# STEP 2 → DYNAMIC FORM
# ─────────────────────────────────────────────
@login_required
def onboarding_stage(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    user_stage = profile.current_stage

    if not user_stage:
        return redirect('onboarding:start')

    # 🔥 Stage flow based on user selection
    stage_flow_map = {
        "school_low": ["school_low"],
        "school_high": ["school_low", "school_high"],
        "undergraduate": ["school_low", "school_high", "undergraduate"],
        "working": ["school_low", "school_high", "undergraduate", "working"],
    }

    required_stages = stage_flow_map.get(user_stage, ["school_low"])

    # 🔥 Find first incomplete stage
    for stage in required_stages:
        if not getattr(profile, f"{stage}_completed", False):
            current_stage = stage
            break
    else:
        # ✅ All stages completed → Dashboard
        return redirect('dashboard:home')

    # 🔥 Dynamic form mapping
    form_map = {
        "school_low": (SchoolLowForm, 20, "Tell us about your 10th"),
        "school_high": (SchoolHighForm, 40, "Your 12th Stream & Subjects"),
        "undergraduate": (UGForm, 70, "Your Degree Details"),
        "working": (CommonForm, 90, "Your Professional Info"),
    }

    FormClass, percent, title = form_map[current_stage]

    if request.method == "POST":
        form = FormClass(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)

            # ✅ Mark stage completed
            setattr(profile, f"{current_stage}_completed", True)
            profile.save()

            # 🔥 Move to next incomplete stage
            return redirect('onboarding:stage')
        else:
            print("❌ FORM ERRORS:", form.errors)

    else:
        form = FormClass(instance=profile)

    return render(request, "onboarding/stage.html", {
        "form": form,
        "percent": percent,
        "title": title
    })