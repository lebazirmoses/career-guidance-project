from django.core.management.base import BaseCommand
from apps.assessments.models import Test, Question, Option


class Command(BaseCommand):
    help = "Seed Advanced Personality Test (Scenario-Based Demo)"

    def handle(self, *args, **kwargs):

        test, created = Test.objects.get_or_create(
            slug="personality-advanced-demo",
            defaults={
                "name": "Personality Assessment (Advanced)",
                "description": "Scenario-based personality test using Big Five traits",
                "category": "personality",
                "test_type": "mcq",
                "time_limit_mins": 15,
                "order": 1,
                "applicable_levels": ["10", "12", "undergraduate"]
            }
        )

        if not created:
            self.stdout.write("Test already exists. Skipping.")
            return

        questions_data = [

# Q1
{
"text": "You are assigned a long-term project with minimal supervision. How do you approach it?",
"options": [
("Plan everything in detail and track progress",
 {"conscientiousness": 1.0, "emotional_stability": 0.6}),
("Start quickly and adjust as you go",
 {"openness": 0.7, "conscientiousness": 0.5}),
("Work only when deadlines approach",
 {"conscientiousness": 0.3}),
("Feel lost without guidance",
 {"emotional_stability": 0.2})
]
},

# Q2
{
"text": "At a social gathering with unfamiliar people, what do you do?",
"options": [
("Initiate conversations confidently",
 {"extraversion": 1.0, "agreeableness": 0.6}),
("Talk when approached",
 {"extraversion": 0.6}),
("Stay quiet and observe",
 {"extraversion": 0.3}),
("Avoid interaction",
 {"extraversion": 0.1})
]
},

# Q3
{
"text": "A sudden change disrupts your plans. Your reaction?",
"options": [
("Adapt quickly and explore new possibilities",
 {"openness": 1.0, "emotional_stability": 0.7}),
("Adjust but feel slightly uneasy",
 {"emotional_stability": 0.5}),
("Resist the change",
 {"openness": 0.3}),
("Feel stressed and frustrated",
 {"emotional_stability": 0.2})
]
},

# Q4
{
"text": "A teammate is struggling and slowing down the group. What do you do?",
"options": [
("Help them and keep team morale high",
 {"agreeableness": 1.0, "extraversion": 0.6}),
("Focus on your own work",
 {"conscientiousness": 0.6}),
("Get annoyed but say nothing",
 {"emotional_stability": 0.3}),
("Complain to others",
 {"agreeableness": 0.2})
]
},

# Q5
{
"text": "You are given a repetitive task for weeks. How do you handle it?",
"options": [
("Stay disciplined and complete efficiently",
 {"conscientiousness": 1.0}),
("Find creative ways to make it interesting",
 {"openness": 0.8}),
("Do it reluctantly",
 {"emotional_stability": 0.4}),
("Lose motivation quickly",
 {"conscientiousness": 0.2})
]
},

# Q6
{
"text": "You receive unexpected negative feedback. What do you do?",
"options": [
("Analyze it and improve yourself",
 {"conscientiousness": 1.0, "emotional_stability": 0.7}),
("Accept but feel slightly affected",
 {"emotional_stability": 0.5}),
("Ignore it",
 {"openness": 0.3}),
("Take it personally",
 {"emotional_stability": 0.2})
]
},

# Q7
{
"text": "You have free time with no responsibilities. What do you prefer?",
"options": [
("Explore new ideas or hobbies",
 {"openness": 1.0}),
("Meet friends and socialize",
 {"extraversion": 0.8}),
("Relax alone",
 {"emotional_stability": 0.5}),
("Scroll aimlessly",
 {"conscientiousness": 0.2})
]
},

# Q8
{
"text": "You are in a disagreement with someone. What is your approach?",
"options": [
("Listen and find common ground",
 {"agreeableness": 1.0, "emotional_stability": 0.7}),
("Defend your opinion strongly",
 {"extraversion": 0.5}),
("Avoid conflict",
 {"emotional_stability": 0.4}),
("Get irritated easily",
 {"emotional_stability": 0.2})
]
},

# Q9
{
"text": "You are asked to lead a team unexpectedly. What do you do?",
"options": [
("Take charge and organize everything",
 {"extraversion": 1.0, "conscientiousness": 0.8}),
("Accept but feel nervous",
 {"emotional_stability": 0.5}),
("Prefer someone else leads",
 {"extraversion": 0.3}),
("Avoid responsibility",
 {"conscientiousness": 0.2})
]
},

# Q10
{
"text": "You face repeated failure in achieving a goal. What do you do?",
"options": [
("Persist and improve strategy",
 {"conscientiousness": 1.0, "emotional_stability": 0.8}),
("Take a break and try later",
 {"emotional_stability": 0.6}),
("Doubt your abilities",
 {"emotional_stability": 0.3}),
("Give up",
 {"conscientiousness": 0.1})
]
},

        ]

        for i, q in enumerate(questions_data, start=1):
            question = Question.objects.create(
                test=test,
                question_text=q["text"],
                question_type="mcq",
                difficulty="medium",   # personality ≠ hard logic
                difficulty_multiplier=1.0,
                order=i
            )

            for idx, (text, scores) in enumerate(q["options"], start=1):
                Option.objects.create(
                    question=question,
                    text=text,
                    scores=scores,
                    order=idx
                )

        self.stdout.write(self.style.SUCCESS("✅ Personality Test Created Successfully"))