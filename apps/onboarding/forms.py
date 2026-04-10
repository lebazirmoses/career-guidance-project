from django import forms
from apps.profiling.models import UserProfile


class StageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["current_stage"]


class SchoolLowForm(forms.ModelForm):
    interests = forms.CharField(help_text="Comma separated")

    class Meta:
        model = UserProfile
        fields = ["class_level", "interests"]

    def clean_interests(self):
        data = self.cleaned_data["interests"]
        return [x.strip() for x in data.split(",") if x.strip()]


class SchoolHighForm(forms.ModelForm):
    subjects = forms.CharField(help_text="Comma separated")
    strong_subjects = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ["stream", "subjects", "strong_subjects"]

    def clean_subjects(self):
        return [x.strip() for x in self.cleaned_data["subjects"].split(",")]

    def clean_strong_subjects(self):
        data = self.cleaned_data.get("strong_subjects", "")
        return [x.strip() for x in data.split(",") if x.strip()]


class UGForm(forms.ModelForm):
    self_rated_skills = forms.CharField(help_text="Python:8, Communication:7")

    class Meta:
        model = UserProfile
        fields = ["degree", "specialization", "self_rated_skills"]

    def clean_self_rated_skills(self):
        raw = self.cleaned_data["self_rated_skills"]
        result = {}

        for item in raw.split(","):
            if ":" in item:
                k, v = item.split(":")
                result[k.strip()] = float(v.strip())

        return result


class WorkingForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["institution", "score", "score_type"]