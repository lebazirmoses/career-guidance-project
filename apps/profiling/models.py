from django.db import models
from django.conf import settings

# ──────────────────────────────
# User Profile
# ──────────────────────────────
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

    # ── Onboarding stages ──
    current_stage = models.CharField(max_length=30, choices=[
        ('school_low', 'Class 6–10'),
        ('school_high', 'Class 11–12'),
        ('undergraduate', 'Undergraduate'),
        ('postgraduate', 'Postgraduate'),
        ('working', 'Working Professional'),
    ], blank=True)

    # Completion flags
    school_low_completed = models.BooleanField(default=False)
    school_high_completed = models.BooleanField(default=False)
    undergraduate_completed = models.BooleanField(default=False)
    postgraduate_completed = models.BooleanField(default=False)
    working_completed = models.BooleanField(default=False)

    # ── SCHOOL LEVEL ──
    class_level = models.IntegerField(null=True, blank=True)
    stream = models.CharField(max_length=30, blank=True)
    subjects = models.JSONField(default=list, blank=True)
    strong_subjects = models.JSONField(default=list, blank=True)
    interests = models.JSONField(default=list, blank=True)
    score = models.FloatField(null=True, blank=True)
    score_type = models.CharField(max_length=20, blank=True)

    # ── UNDERGRADUATE / POSTGRADUATE ──
    degree_choices = [
        ('ba', 'Bachelor of Arts'),
        ('bsc', 'Bachelor of Science'),
        ('bcom', 'Bachelor of Commerce'),
        ('btech', 'B.Tech / B.E.'),
        ('mbbs', 'Medicine (MBBS)'),
        ('bds', 'Dental Surgery (BDS)'),
        ('other', 'Other'),
    ]
    degree = models.CharField(max_length=50, choices=degree_choices, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=200, blank=True)
    institution_type = models.CharField(max_length=50, blank=True)
    self_rated_skills = models.JSONField(default=dict, blank=True)

    # ── AI FLAGS ──
    has_maths = models.BooleanField(default=False)
    has_biology = models.BooleanField(default=False)
    has_commerce = models.BooleanField(default=False)

    # ── Degree → Specialization Mapping ──
    specializations_map = {
        'ba': ['English', 'History', 'Political Science', 'Psychology', 'Economics', 'Journalism', 'Sociology', 'Arts'],
        'bsc': ['Computer Science', 'Biotechnology', 'Agriculture', 'Nursing', 'Physics', 'Chemistry', 'Mathematics', 'Microbiology', 'Forensic Science', 'Food Technology'],
        'bcom': ['Accounting & Finance', 'Banking & Insurance', 'Taxation', 'International Business', 'Business Analytics', 'Computer Applications'],
        'btech': ['CSE', 'ECE', 'Mechanical', 'Civil', 'AI & Data Science', 'Cyber Security', 'Biotechnology', 'Aerospace', 'Mechatronics', 'Automotive Engineering', 'Food Technology'],
        'mbbs': ['General Medicine', 'Surgery', 'Pediatrics', 'Cardiology'],
        'bds': ['Dental Surgery', 'Oral Health'],
        'other': [],
    }

    # ── METHODS ──
    def save(self, *args, **kwargs):
        subjects_text = " ".join(self.subjects).lower()
        self.has_maths = "math" in subjects_text
        self.has_biology = "bio" in subjects_text
        self.has_commerce = self.stream.lower() == "commerce" if self.stream else False

        name = (self.institution or "").lower()
        if "school" in name:
            self.institution_type = "school"
        elif "college" in name:
            self.institution_type = "college"
        elif "university" in name:
            self.institution_type = "university"
        else:
            self.institution_type = "other"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.full_name} Profile"


# ──────────────────────────────
# Trait Vector – AI Computation
# ──────────────────────────────
class TraitVector(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='trait_vector')

    # Cognitive traits
    logical_reasoning   = models.FloatField(default=0.0)
    verbal_ability      = models.FloatField(default=0.0)
    numerical_aptitude  = models.FloatField(default=0.0)
    spatial_reasoning   = models.FloatField(default=0.0)
    memory_retention    = models.FloatField(default=0.0)
    processing_speed    = models.FloatField(default=0.0)

    # Personality traits (Big Five)
    openness            = models.FloatField(default=0.0)
    conscientiousness   = models.FloatField(default=0.0)
    extraversion        = models.FloatField(default=0.0)
    agreeableness       = models.FloatField(default=0.0)
    neuroticism         = models.FloatField(default=0.0)

    # Holland RIASEC
    realistic           = models.FloatField(default=0.0)
    investigative       = models.FloatField(default=0.0)
    artistic            = models.FloatField(default=0.0)
    social              = models.FloatField(default=0.0)
    enterprising        = models.FloatField(default=0.0)
    conventional        = models.FloatField(default=0.0)

    # Behavioral traits
    leadership          = models.FloatField(default=0.0)
    teamwork            = models.FloatField(default=0.0)
    creativity          = models.FloatField(default=0.0)
    resilience          = models.FloatField(default=0.0)
    empathy             = models.FloatField(default=0.0)
    risk_appetite       = models.FloatField(default=0.0)
    attention_to_detail = models.FloatField(default=0.0)
    communication       = models.FloatField(default=0.0)

    # Motivational drivers
    intrinsic_motivation = models.FloatField(default=0.0)
    extrinsic_motivation = models.FloatField(default=0.0)
    social_impact_drive  = models.FloatField(default=0.0)
    autonomy_preference  = models.FloatField(default=0.0)

    confidence_score    = models.FloatField(default=0.0)
    last_updated        = models.DateTimeField(auto_now=True)

    def to_dict(self):
        exclude = {'id', 'user_id', 'user', 'confidence_score', 'last_updated'}
        return {f.name: float(getattr(self, f.name) or 0.0)
                for f in self._meta.fields if f.name not in exclude}

    def __str__(self):
        return f"Traits: {self.user.full_name} (confidence: {self.confidence_score:.0%})"


# ──────────────────────────────
# Career Model
# ──────────────────────────────
class Career(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    min_education = models.CharField(max_length=50, choices=[
        ('10th', '10th Standard'),
        ('12th', '12th Standard'),
        ('UG', 'Undergraduate')
    ])

    # Cognitive & RIASEC targets
    target_logic = models.FloatField(default=0.0)
    target_numerical = models.FloatField(default=0.0)
    target_verbal = models.FloatField(default=0.0)
    target_spatial = models.FloatField(default=0.0)

    target_investigative = models.FloatField(default=0.0)
    target_realistic = models.FloatField(default=0.0)
    target_artistic = models.FloatField(default=0.0)
    target_social = models.FloatField(default=0.0)
    target_enterprising = models.FloatField(default=0.0)
    target_conventional = models.FloatField(default=0.0)

    target_leadership = models.FloatField(default=0.0)
    target_teamwork = models.FloatField(default=0.0)
    target_communication = models.FloatField(default=0.0)

    roadmap_steps = models.JSONField(default=list, blank=True)

    def get_vector(self):
        return {
            'logical_reasoning': self.target_logic,
            'numerical_aptitude': self.target_numerical,
            'verbal_ability': self.target_verbal,
            'spatial_reasoning': self.target_spatial,
            'investigative': self.target_investigative,
            'realistic': self.target_realistic,
            'artistic': self.target_artistic,
            'social': self.target_social,
            'enterprising': self.target_enterprising,
            'conventional': self.target_conventional,
            'leadership': self.target_leadership,
            'teamwork': self.target_teamwork,
            'communication': self.target_communication,
        }

    def __str__(self):
        return self.name