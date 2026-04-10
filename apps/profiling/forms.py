from django import forms
from .models import UserProfile

# ───────────── Stage Selection ─────────────
class StageSelectionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["current_stage"]
        widgets = {"current_stage": forms.Select(attrs={"class": "form-control"})}


# ───────────── School Low (6th–10th) ─────────────
class SchoolLowForm(forms.ModelForm):
    CLASS_LEVEL_CHOICES = [(i, f"Class {i}") for i in range(6, 11)]
    SUBJECT_CHOICES = ['Maths', 'Physics', 'Chemistry', 'Biology', 'Social Science']

    class_level = forms.ChoiceField(choices=CLASS_LEVEL_CHOICES)
    institution = forms.CharField()
    subjects = forms.MultipleChoiceField(
        choices=[(s, s) for s in SUBJECT_CHOICES],
        widget=forms.CheckboxSelectMultiple,
        initial=SUBJECT_CHOICES
    )
    strong_subjects = forms.MultipleChoiceField(
        choices=[(s, s) for s in SUBJECT_CHOICES],
        widget=forms.CheckboxSelectMultiple
    )
    interests = forms.MultipleChoiceField(
        choices=[(s, s) for s in SUBJECT_CHOICES],
        widget=forms.CheckboxSelectMultiple
    )
    score = forms.FloatField()
    score_type = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['class_level', 'institution', 'subjects', 'strong_subjects', 'interests', 'score', 'score_type']

    def clean(self):
        cleaned_data = super().clean()
        subjects = cleaned_data.get('subjects', [])
        strong_subjects = cleaned_data.get('strong_subjects', [])
        interests = cleaned_data.get('interests', [])
        if not set(strong_subjects).issubset(set(subjects)):
            self.add_error('strong_subjects', "Strong subjects must be selected from your subjects studied.")
        if not set(interests).issubset(set(subjects)):
            self.add_error('interests', "Interests must be selected from your subjects studied.")


# ───────────── School High (11th–12th) ─────────────
class SchoolHighForm(forms.ModelForm):
    STREAM_CHOICES = [
        ('science_eng', 'Science - Engineering (PCM+CS)'),
        ('science_med', 'Science - Medical/Bio (PCB/PCMB)'),
        ('commerce_main', 'Commerce - Accountancy/Economics/Maths'),
        ('arts', 'Arts / Humanities'),
        ('vocational', 'Vocational / Career-oriented')
    ]
    SUBJECTS_MAP = {
        'science_eng': ['Physics', 'Chemistry', 'Mathematics', 'Computer Science'],
        'science_med': ['Physics', 'Chemistry', 'Biology', 'Mathematics'],
        'commerce_main': ['Accountancy', 'Economics', 'Business Studies', 'Mathematics'],
        'arts': ['History', 'Geography', 'Political Science', 'Economics', 'Psychology'],
        'vocational': ['Nursing', 'Textiles', 'Financial Management', 'Computer Applications'],
    }

    stream = forms.ChoiceField(choices=STREAM_CHOICES)
    institution = forms.CharField()
    subjects = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)
    strong_subjects = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)
    interests = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)
    score = forms.FloatField()
    score_type = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['stream', 'institution', 'subjects', 'strong_subjects', 'interests', 'score', 'score_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        stream = self.data.get('stream') or getattr(self.instance, 'stream', None)
        if stream in self.SUBJECTS_MAP:
            choices = [(s, s) for s in self.SUBJECTS_MAP[stream]]
            self.fields['subjects'].choices = choices
            self.fields['strong_subjects'].choices = choices
            self.fields['interests'].choices = choices

    def clean(self):
        cleaned_data = super().clean()
        subjects = cleaned_data.get('subjects', [])
        strong_subjects = cleaned_data.get('strong_subjects', [])
        interests = cleaned_data.get('interests', [])
        if not set(strong_subjects).issubset(set(subjects)):
            self.add_error('strong_subjects', "Strong subjects must be selected from your subjects studied.")
        if not set(interests).issubset(set(subjects)):
            self.add_error('interests', "Interests must be selected from your subjects studied.")


# ───────────── Undergraduate (UG) ─────────────
class UGForm(forms.ModelForm):
    SKILL_CHOICES = ['Python', 'AI', 'ML', 'Data Science', 'NLP', 'Statistics']

    self_rated_skills = forms.MultipleChoiceField(
        choices=[(s, s) for s in SKILL_CHOICES],
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = UserProfile
        fields = ['degree', 'specialization', 'institution', 'subjects', 'strong_subjects', 'self_rated_skills', 'interests', 'score', 'score_type']

    def clean_self_rated_skills(self):
        # Convert list to dict with default rating 8 if needed
        skills = self.cleaned_data.get('self_rated_skills', [])
        return {skill: 8 for skill in skills}


# ───────────── Postgrad / Working Professional ─────────────
class CommonForm(forms.ModelForm):
    SKILL_CHOICES = ['Python', 'AI', 'ML', 'Data Science', 'NLP', 'Statistics']

    self_rated_skills = forms.MultipleChoiceField(
        choices=[(s, s) for s in SKILL_CHOICES],
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = UserProfile
        fields = ['institution', 'degree', 'specialization', 'self_rated_skills', 'interests']