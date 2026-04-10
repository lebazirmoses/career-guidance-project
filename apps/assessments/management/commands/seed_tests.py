from django.core.management.base import BaseCommand
from apps.assessments.models import Test, Question


class Command(BaseCommand):
    help = 'Seeds full psychometric assessment suite for FutureAI'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.WARNING("🚀 Seeding assessments..."))

        # ---------- COMMON ----------
        LEVELS = ["10th", "12th", "Undergraduate"]

        # =========================================================
        # 1. PERSONALITY TEST (BIG FIVE)
        # =========================================================
        personality_test, created = Test.objects.get_or_create(
            slug='personality-diagnostic',
            defaults={
                'name': 'Core Personality Diagnostic',
                'description': 'Maps your behavioral traits and work style.',
                'category': 'personality',
                'test_type': 'mcq',
                'order': 1,
                'applicable_levels': LEVELS
            }
        )

        if created:
            questions = [
                {
                    "text": "I enjoy social gatherings and meeting new people.",
                    "mapping": {"extraversion": 0.4},
                },
                {
                    "text": "I like to keep my work organized and planned.",
                    "mapping": {"conscientiousness": 0.5},
                },
                {
                    "text": "I remain calm under pressure.",
                    "mapping": {"emotional_stability": 0.5},
                },
                {
                    "text": "I enjoy trying new and creative ideas.",
                    "mapping": {"openness": 0.5},
                },
                {
                    "text": "I am considerate and helpful toward others.",
                    "mapping": {"agreeableness": 0.5},
                }
            ]

            for q in questions:
                Question.objects.create(
                    test=personality_test,
                    question_text=q["text"],
                    trait_mapping=q["mapping"],
                    options=["1", "2", "3", "4", "5"],
                    is_active=True
                )

            self.stdout.write(self.style.SUCCESS("✅ Personality Test created"))

        # =========================================================
        # 2. COGNITIVE TEST
        # =========================================================
        cognitive_test, created = Test.objects.get_or_create(
            slug='cognitive-aptitude',
            defaults={
                'name': 'Cognitive Ability Test',
                'description': 'Tests logic, math, and reasoning ability.',
                'category': 'cognitive',
                'test_type': 'mcq',
                'order': 2,
                'applicable_levels': LEVELS
            }
        )

        if created:
            questions = [
                {
                    "text": "What is 12 + 15?",
                    "options": ["25", "27", "30", "32"],
                    "answer": "27",
                    "mapping": {"numerical": 0.9}
                },
                {
                    "text": "Find next: 2, 4, 8, 16, ?",
                    "options": ["18", "24", "32", "20"],
                    "answer": "32",
                    "mapping": {"logical_reasoning": 0.9}
                },
                {
                    "text": "If all A are B and all B are C, then A are C?",
                    "options": ["True", "False"],
                    "answer": "True",
                    "mapping": {"logical_reasoning": 0.8}
                }
            ]

            for q in questions:
                Question.objects.create(
                    test=cognitive_test,
                    question_text=q["text"],
                    options=q["options"],
                    correct_answer=q["answer"],
                    trait_mapping=q["mapping"],
                    is_active=True
                )

            self.stdout.write(self.style.SUCCESS("✅ Cognitive Test created"))

        # =========================================================
        # 3. RIASEC INTEREST TEST
        # =========================================================
        interest_test, created = Test.objects.get_or_create(
            slug='career-interest',
            defaults={
                'name': 'Career Interest Profiler',
                'description': 'Identifies what type of work you enjoy.',
                'category': 'interest',
                'test_type': 'mcq',
                'order': 3,
                'applicable_levels': LEVELS
            }
        )

        if created:
            questions = [
                {
                    "text": "Which do you prefer?",
                    "options": ["Fix a machine", "Write a story"],
                    "mapping": {"realistic": 0.5, "artistic": 0.5}
                },
                {
                    "text": "Which do you enjoy more?",
                    "options": ["Analyze data", "Help people"],
                    "mapping": {"investigative": 0.6, "social": 0.6}
                },
                {
                    "text": "Choose one:",
                    "options": ["Start a business", "Organize files"],
                    "mapping": {"enterprising": 0.6, "conventional": 0.6}
                }
            ]

            for q in questions:
                Question.objects.create(
                    test=interest_test,
                    question_text=q["text"],
                    options=q["options"],
                    trait_mapping=q["mapping"],
                    is_active=True
                )

            self.stdout.write(self.style.SUCCESS("✅ Interest Test created"))

        # =========================================================
        # 4. EMOTIONAL INTELLIGENCE TEST
        # =========================================================
        eq_test, created = Test.objects.get_or_create(
            slug='emotional-intelligence',
            defaults={
                'name': 'Emotional Intelligence Test',
                'description': 'Measures empathy, teamwork, and resilience.',
                'category': 'personality',
                'test_type': 'mcq',
                'order': 4,
                'applicable_levels': LEVELS
            }
        )

        if created:
            questions = [
                {
                    "text": "A teammate is struggling. What do you do?",
                    "options": [
                        "Ignore",
                        "Help them",
                        "Report them",
                        "Take over their work"
                    ],
                    "mapping": {"empathy": 0.6, "teamwork": 0.6}
                },
                {
                    "text": "You fail a test. What next?",
                    "options": [
                        "Give up",
                        "Try again",
                        "Blame others",
                        "Ignore it"
                    ],
                    "mapping": {"resilience": 0.7}
                }
            ]

            for q in questions:
                Question.objects.create(
                    test=eq_test,
                    question_text=q["text"],
                    options=q["options"],
                    trait_mapping=q["mapping"],
                    is_active=True
                )

            self.stdout.write(self.style.SUCCESS("✅ EQ Test created"))

        # =========================================================
        # 5. WORK VALUES TEST
        # =========================================================
        values_test, created = Test.objects.get_or_create(
            slug='work-values',
            defaults={
                'name': 'Workplace Values Assessment',
                'description': 'Identifies what matters most in your career.',
                'category': 'personality',
                'test_type': 'mcq',
                'order': 5,
                'applicable_levels': LEVELS
            }
        )

        if created:
            questions = [
                {
                    "text": "I prefer flexible working hours.",
                    "mapping": {"work_life_balance": 0.6}
                },
                {
                    "text": "High salary is very important to me.",
                    "mapping": {"financial_motivation": 0.7}
                },
                {
                    "text": "I want my work to create social impact.",
                    "mapping": {"purpose_driven": 0.7}
                }
            ]

            for q in questions:
                Question.objects.create(
                    test=values_test,
                    question_text=q["text"],
                    options=["1", "2", "3", "4", "5"],
                    trait_mapping=q["mapping"],
                    is_active=True
                )

            self.stdout.write(self.style.SUCCESS("✅ Values Test created"))

        self.stdout.write(self.style.SUCCESS("🎯 ALL TESTS SEEDED SUCCESSFULLY!"))