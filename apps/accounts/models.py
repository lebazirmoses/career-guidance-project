from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    # ── Education level choices (Indian system) ───────────────────────────────
    class EducationLevel(models.TextChoices):
        MIDDLE_SCHOOL  = 'middle_school',  'Middle School (6–8th)'
        HIGH_SCHOOL    = 'high_school',    'High School (9–10th / SSLC)'
        HIGHER_SEC     = 'higher_sec',     'Higher Secondary (11–12th / +2)'
        UNDERGRADUATE  = 'undergraduate',  'Undergraduate (UG)'
        POSTGRADUATE   = 'postgraduate',   'Postgraduate (PG)'
        WORKING        = 'working',        'Working Professional'
        OTHER          = 'other',          'Other'

    class Role(models.TextChoices):
        STUDENT    = 'student',    'Student'
        JOB_SEEKER = 'job_seeker', 'Job Seeker'
        ADMIN      = 'admin',      'Admin'

    class Gender(models.TextChoices):
        MALE        = 'male',        'Male'
        FEMALE      = 'female',      'Female'
        NON_BINARY  = 'non_binary',  'Non-Binary'
        PREFER_NOT  = 'prefer_not',  'Prefer not to say'

    # ── Core fields ───────────────────────────────────────────────────────────
    email           = models.EmailField(unique=True)
    phone           = models.CharField(max_length=15, blank=True)
    full_name       = models.CharField(max_length=150)
    date_of_birth   = models.DateField(null=True, blank=True)
    gender          = models.CharField(max_length=20, choices=Gender.choices, blank=True)
    state           = models.CharField(max_length=100, blank=True)   # Indian state
    city            = models.CharField(max_length=100, blank=True)

    # ── Classification ────────────────────────────────────────────────────────
    role            = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    education_level = models.CharField(max_length=25, choices=EducationLevel.choices, blank=True)

    # ── Onboarding state ──────────────────────────────────────────────────────
    onboarding_complete   = models.BooleanField(default=False)
    onboarding_stage      = models.PositiveSmallIntegerField(default=0)  # 0–4
    profile_complete      = models.BooleanField(default=False)

    # ── System fields ─────────────────────────────────────────────────────────
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    date_joined   = models.DateTimeField(auto_now_add=True)
    last_login    = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    @property
    def age(self):
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None