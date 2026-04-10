from django.db import models
from django.conf import settings


# ──────────────────────────────
# Test Types
# ──────────────────────────────
class TestType(models.TextChoices):
    MCQ         = 'mcq',         'Multiple Choice (MCQ)'
    TIMED       = 'timed',       'Timed Aptitude'
    SCENARIO    = 'scenario',    'Scenario-Based'
    DRAG_RANK   = 'drag_rank',   'Drag & Rank'
    FREE_TEXT   = 'free_text',   'Free Text (AI-Analyzed)'


# ──────────────────────────────
# Test Model
# ──────────────────────────────
class Test(models.Model):

    class Category(models.TextChoices):
        COGNITIVE   = 'cognitive',   'Cognitive Ability'
        PERSONALITY = 'personality', 'Personality'
        INTEREST    = 'interest',    'Interest & Holland'
        EMOTIONAL   = 'emotional',   'Emotional Intelligence'
        BEHAVIORAL  = 'behavioral',  'Behavioral'
        CREATIVE    = 'creative',    'Creativity'

    name            = models.CharField(max_length=100)
    slug            = models.SlugField(unique=True)
    description     = models.TextField(blank=True)

    category        = models.CharField(max_length=20, choices=Category.choices)
    test_type       = models.CharField(max_length=20, choices=TestType.choices)

    is_mandatory    = models.BooleanField(default=False)
    time_limit_mins = models.PositiveIntegerField(null=True, blank=True)

    order           = models.PositiveSmallIntegerField(default=0)

    # JSON → ["10", "12", "undergraduate"]
    applicable_levels = models.JSONField(default=list)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{'[M]' if self.is_mandatory else '[O]'} {self.name}"


# ──────────────────────────────
# Question Model
# ──────────────────────────────
class Question(models.Model):
    
    class Section(models.TextChoices):
        COGNITIVE   = 'cognitive', 'Cognitive'
        EMOTIONAL   = 'emotional', 'Emotional'
        BEHAVIORAL  = 'behavioral', 'Behavioral'
        PERSONALITY = 'personality', 'Personality'

    section = models.CharField(
        max_length=20,
        choices=Section.choices,
        default=Section.BEHAVIORAL
    )

    class DifficultyLevel(models.TextChoices):
        EASY    = 'easy',   'Easy'
        MEDIUM  = 'medium', 'Medium'
        HARD    = 'hard',   'Hard'

    test            = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question_text   = models.TextField()
    question_type   = models.CharField(max_length=20, choices=TestType.choices)

    difficulty      = models.CharField(max_length=10, choices=DifficultyLevel.choices,
                                       default=DifficultyLevel.MEDIUM)

    # 🔥 NEW: important for scoring weight
    difficulty_multiplier = models.FloatField(default=1.0)

    # Optional fallback mapping (rarely used now)
    trait_mapping  = models.JSONField(default=dict, blank=True)

    order          = models.PositiveSmallIntegerField(default=0)
    is_active      = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Q{self.order}: {self.question_text[:60]}"


# ──────────────────────────────
# Option Model (🔥 MOST IMPORTANT)
# ──────────────────────────────
class Option(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text     = models.CharField(max_length=255)

    scores   = models.JSONField(default=dict)

    is_correct = models.BooleanField(default=False)

    weight = models.FloatField(default=1.0)  # 🔥 NEW

    meta = models.JSONField(default=dict, blank=True)  # 🔥 NEW

    order   = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.text[:50]}"


# ──────────────────────────────
# User Test Attempt
# ──────────────────────────────
class UserTestAttempt(models.Model):

    class Status(models.TextChoices):
        NOT_STARTED = 'not_started', 'Not Started'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED   = 'completed',   'Completed'
        SKIPPED     = 'skipped',     'Skipped'

    user        = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='test_attempts')

    test        = models.ForeignKey(Test, on_delete=models.CASCADE)

    status      = models.CharField(max_length=15,
                                  choices=Status.choices,
                                  default=Status.NOT_STARTED)

    started_at  = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    time_taken_secs = models.PositiveIntegerField(null=True, blank=True)

    # 🔥 FINAL OUTPUT OF TEST
    trait_scores = models.JSONField(default=dict)

    # AI outputs (future GPT / ML)
    ai_analysis  = models.JSONField(default=dict, blank=True)

    class Meta:
        unique_together = ('user', 'test')

    def __str__(self):
        return f"{self.user} → {self.test.name} [{self.status}]"


# ──────────────────────────────
# User Answer
# ──────────────────────────────
class UserAnswer(models.Model):

    attempt  = models.ForeignKey(UserTestAttempt,
                                 on_delete=models.CASCADE,
                                 related_name='answers')

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # 🔥 CRITICAL CHANGE
    selected_option = models.ForeignKey(Option,
                                        on_delete=models.CASCADE,
                                        null=True, blank=True)

    # For FREE_TEXT answers
    answer_text = models.TextField(blank=True)

    is_correct  = models.BooleanField(null=True, blank=True)

    time_taken_secs = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"UserAnswer → Q{self.question.order}"