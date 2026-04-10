from django.core.management.base import BaseCommand
from apps.assessments.models import Test, Question

class Command(BaseCommand):
    help = "Seed assessments and questions"

    def handle(self, *args, **kwargs):
        self.stdout.write("🌱 Seeding assessments...")

        # =====================================================
        # 🔹 TEST 1: Cognitive
        # =====================================================
        cognitive_test, _ = Test.objects.get_or_create(
            slug="cognitive-ability",
            defaults={
                "name": "Cognitive Ability Test",
                "description": "Test your logical, numerical, and verbal skills.",
                "category": "cognitive",
                "test_type": "mcq",
                "is_mandatory": True,
                "time_limit_mins": 20,
                "applicable_levels": ["school_high", "undergraduate"],
                "order": 1,
            }
        )

        cognitive_questions = [
            {
                "question_text": "Find the next number: 2, 6, 12, 20, ?",
                "options": [
                    {"text": "28", "traits": {"numerical_aptitude": 0.9}},
                    {"text": "30", "traits": {"numerical_aptitude": 0.3}},
                    {"text": "24", "traits": {"numerical_aptitude": 0.2}},
                    {"text": "26", "traits": {"numerical_aptitude": 0.1}},
                ],
            },
            {
                "question_text": "Which word is closest to 'analyze'?",
                "options": [
                    {"text": "Break down", "traits": {"verbal_ability": 0.9}},
                    {"text": "Ignore", "traits": {"verbal_ability": 0.1}},
                    {"text": "Combine", "traits": {"verbal_ability": 0.3}},
                    {"text": "Build", "traits": {"verbal_ability": 0.2}},
                ],
            },
        ]

        self.create_questions(cognitive_test, cognitive_questions)

        # =====================================================
        # 🔹 TEST 2: Personality (Big Five)
        # =====================================================
        personality_test, _ = Test.objects.get_or_create(
            slug="personality-big-five",
            defaults={
                "name": "Personality Test (Big Five)",
                "description": "Understand your personality traits.",
                "category": "personality",
                "test_type": "mcq",
                "is_mandatory": True,
                "applicable_levels": ["school_high", "undergraduate", "working"],
                "order": 2,
            }
        )

        personality_questions = [
            {
                "question_text": "I enjoy trying new experiences.",
                "options": [
                    {"text": "Strongly Agree", "traits": {"openness": 1.0}},
                    {"text": "Agree", "traits": {"openness": 0.7}},
                    {"text": "Neutral", "traits": {"openness": 0.5}},
                    {"text": "Disagree", "traits": {"openness": 0.2}},
                ],
            },
            {
                "question_text": "I keep my work organized.",
                "options": [
                    {"text": "Strongly Agree", "traits": {"conscientiousness": 1.0}},
                    {"text": "Agree", "traits": {"conscientiousness": 0.7}},
                    {"text": "Neutral", "traits": {"conscientiousness": 0.5}},
                    {"text": "Disagree", "traits": {"conscientiousness": 0.2}},
                ],
            },
        ]

        self.create_questions(personality_test, personality_questions)

        # =====================================================
        # 🔹 TEST 3: Interest (RIASEC)
        # =====================================================
        interest_test, _ = Test.objects.get_or_create(
            slug="interest-riasec",
            defaults={
                "name": "Interest Assessment",
                "description": "Discover your career interests.",
                "category": "interest",
                "test_type": "mcq",
                "is_mandatory": True,
                "applicable_levels": ["school_high", "undergraduate"],
                "order": 3,
            }
        )

        interest_questions = [
            {
                "question_text": "Which activity do you enjoy most?",
                "options": [
                    {"text": "Fixing machines", "traits": {"realistic": 0.9}},
                    {"text": "Researching problems", "traits": {"investigative": 0.9}},
                    {"text": "Creating art", "traits": {"artistic": 0.9}},
                    {"text": "Helping people", "traits": {"social": 0.9}},
                ],
            }
        ]

        self.create_questions(interest_test, interest_questions)

        # =====================================================
        # 🔹 TEST 4: Behavioral
        # =====================================================
        behavioral_test, _ = Test.objects.get_or_create(
            slug="behavioral-test",
            defaults={
                "name": "Behavioral Assessment",
                "description": "Understand your behavior patterns.",
                "category": "behavioral",
                "test_type": "mcq",
                "is_mandatory": False,
                "applicable_levels": ["school_high", "undergraduate"],
                "order": 4,
            }
        )

        behavioral_questions = [
            {
                "question_text": "You are given a group project. What do you do?",
                "options": [
                    {"text": "Lead the team", "traits": {"leadership": 0.9}},
                    {"text": "Collaborate", "traits": {"teamwork": 0.9}},
                    {"text": "Work alone", "traits": {"independence": 0.7}},
                    {"text": "Avoid", "traits": {"resilience": 0.1}},
                ],
            }
        ]

        self.create_questions(behavioral_test, behavioral_questions)

        self.stdout.write(self.style.SUCCESS("✅ Seeding completed!"))

    # =====================================================
    # 🔧 HELPER FUNCTION
    # =====================================================
    def create_questions(self, test, questions):
        for i, q in enumerate(questions):
            Question.objects.get_or_create(
                test=test,
                question_text=q["question_text"],
                defaults={
                    "question_type": "mcq",
                    "difficulty": "medium",
                    "options": q["options"],
                    "order": i
                }
            )