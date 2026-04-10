from django.db import models


# =========================================================
# 🔹 CAREER MODEL (AI MATCHING)
# =========================================================
class Career(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Trait mapping (0 → 1 scale)
    required_logic = models.FloatField(default=0.0)
    required_creativity = models.FloatField(default=0.0)
    required_social = models.FloatField(default=0.0)
    required_verbal = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


# =========================================================
# 🔹 CAREER TREE NODE (NEW - DYNAMIC TREE)
# =========================================================
class CareerNode(models.Model):
    STAGE_CHOICES = [
        ("school", "School"),
        ("stream", "Stream"),
        ("ug", "Undergraduate"),
        ("pg", "Postgraduate"),
        ("career", "Career"),
        ("specialization", "Specialization"),
    ]

    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES)
    

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    description = models.TextField(blank=True)

    required_skills = models.JSONField(default=dict, blank=True)

    # ✅ NEW (IMPORTANT)
    is_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.stage})"