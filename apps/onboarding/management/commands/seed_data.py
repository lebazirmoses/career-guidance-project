from django.core.management.base import BaseCommand
from apps.assessments.models import Test, Question

class Command(BaseCommand):
    help = 'Seeds initial career and personality tests'

    def handle(self, *args, **kwargs):
        # 1. Create a Personality Test
        test, created = Test.objects.get_or_create(
            slug='personality-core',
            defaults={
                'name': 'Core Personality Assessment',
                'description': 'Understand your behavioral traits and work style.',
                'category': 'personality',
                'test_type': 'mcq',
            }
        )

        if created:
            questions = [
                {
                    "text": "I enjoy solving complex logical puzzles.",
                    "mapping": {"logical_reasoning": 0.2, "investigative": 0.1},
                    "opts": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
                },
                {
                    "text": "I find it easy to empathize with others' problems.",
                    "mapping": {"empathy": 0.2, "social": 0.2},
                    "opts": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
                },
                {
                    "text": "I prefer working in a highly organized and structured environment.",
                    "mapping": {"conscientiousness": 0.2, "conventional": 0.2},
                    "opts": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
                }
            ]
            for q in questions:
                Question.objects.create(
                    test=test,
                    question_text=q['text'],
                    trait_mapping=q['mapping'],
                    options=q['opts']
                )
            self.stdout.write(self.style.SUCCESS('Successfully seeded Personality Test'))