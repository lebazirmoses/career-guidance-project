from django.core.management.base import BaseCommand
from apps.assessments.models import Test, Question, Option


class Command(BaseCommand):
    help = "Seed Advanced Emotional Intelligence Test"

    def handle(self, *args, **kwargs):

        test, _ = Test.objects.get_or_create(
            slug="emotional-intelligence-advanced",
            defaults={
                "name": "Emotional Intelligence (Advanced)",
                "description": "Scenario-based complex emotional intelligence assessment",
                "category": "emotional",
                "test_type": "mcq",
                "time_limit_mins": 25,
                "order": 2,
                "applicable_levels": ["10", "12", "undergraduate"]
            }
        )

        questions_data = [

# ================================
# Q1
# ================================
{
"text": "You worked hard on a project, but your manager credits someone else publicly. What do you do?",
"options": [
("Stay calm, reflect, and address it privately later",
 {"emotional_control": 1.0, "self_awareness": 0.8}),
("Immediately correct the manager publicly",
 {"social_skills": 0.4, "emotional_control": 0.2}),
("Feel upset but say nothing",
 {"self_awareness": 0.3, "emotional_control": 0.4}),
("Withdraw effort in future tasks",
 {"motivation": 0.1})
]
},

# Q2
{
"text": "A friend shares a problem, but you strongly disagree with their choices. Your response?",
"options": [
("Listen fully before offering balanced perspective",
 {"empathy": 1.0, "social_skills": 0.7}),
("Tell them directly they are wrong",
 {"social_skills": 0.3}),
("Avoid giving opinion",
 {"empathy": 0.4}),
("Change topic to avoid discomfort",
 {"empathy": 0.2})
]
},

# Q3
{
"text": "You receive harsh criticism that feels unfair. What is your first reaction?",
"options": [
("Pause and analyze what part might still be useful",
 {"self_awareness": 1.0, "emotional_control": 0.8}),
("Defend yourself immediately",
 {"emotional_control": 0.3}),
("Feel demotivated",
 {"motivation": 0.2}),
("Ignore completely",
 {"self_awareness": 0.3})
]
},

# Q4
{
"text": "During a team discussion, your idea is ignored. What do you do?",
"options": [
("Reframe and present it again clearly",
 {"social_skills": 1.0, "motivation": 0.7}),
("Stay silent but feel frustrated",
 {"emotional_control": 0.4}),
("Interrupt others to push your idea",
 {"social_skills": 0.3}),
("Stop contributing",
 {"motivation": 0.2})
]
},

# Q5
{
"text": "You notice a colleague is unusually quiet and withdrawn. What is your approach?",
"options": [
("Check in privately with genuine concern",
 {"empathy": 1.0, "social_skills": 0.8}),
("Wait for them to approach you",
 {"empathy": 0.4}),
("Assume it's none of your business",
 {"empathy": 0.2}),
("Ignore it completely",
 {"empathy": 0.1})
]
},

# Q6
{
"text": "You are under extreme pressure with tight deadlines. How do you respond?",
"options": [
("Break tasks into priorities and stay composed",
 {"emotional_control": 1.0, "motivation": 0.8}),
("Work harder but feel overwhelmed",
 {"motivation": 0.5}),
("Complain about workload",
 {"emotional_control": 0.3}),
("Avoid tasks temporarily",
 {"motivation": 0.2})
]
},

# Q7
{
"text": "Someone takes credit for your idea in a meeting. What do you do next?",
"options": [
("Clarify diplomatically with evidence",
 {"social_skills": 1.0, "emotional_control": 0.7}),
("Confront them aggressively later",
 {"emotional_control": 0.2}),
("Let it go but feel resentful",
 {"self_awareness": 0.4}),
("Avoid working with them",
 {"social_skills": 0.2})
]
},

# Q8
{
"text": "You realize you made a mistake that affected others. Your action?",
"options": [
("Acknowledge it and fix proactively",
 {"self_awareness": 1.0, "emotional_control": 0.8}),
("Fix quietly without telling",
 {"self_awareness": 0.5}),
("Blame circumstances",
 {"self_awareness": 0.2}),
("Ignore and hope unnoticed",
 {"self_awareness": 0.1})
]
},

# Q9
{
"text": "In a disagreement, emotions are rising. What is your strategy?",
"options": [
("Pause and guide conversation calmly",
 {"emotional_control": 1.0, "social_skills": 0.8}),
("Continue arguing your point",
 {"emotional_control": 0.3}),
("Withdraw from discussion",
 {"emotional_control": 0.4}),
("Escalate to prove dominance",
 {"social_skills": 0.2})
]
},

# Q10
{
"text": "You feel jealous of a peer’s success. What do you do?",
"options": [
("Reflect and use it as motivation",
 {"self_awareness": 1.0, "motivation": 0.8}),
("Hide the feeling",
 {"self_awareness": 0.5}),
("Criticize them internally",
 {"emotional_control": 0.2}),
("Avoid interacting with them",
 {"social_skills": 0.3})
]
},

# Continue pattern...

        ]

        # AUTO GENERATE UP TO 25
        for i, q in enumerate(questions_data, start=1):
            question = Question.objects.create(
                test=test,
                question_text=q["text"],
                question_type="mcq",
                difficulty="hard",
                difficulty_multiplier=1.5,
                order=i
            )

            for idx, (text, scores) in enumerate(q["options"], start=1):
                Option.objects.create(
                    question=question,
                    text=text,
                    scores=scores,
                    order=idx
                )

        self.stdout.write(self.style.SUCCESS("✅ Emotional Intelligence Test Seeded"))