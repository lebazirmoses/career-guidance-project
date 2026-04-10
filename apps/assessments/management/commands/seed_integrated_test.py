from django.core.management.base import BaseCommand
from apps.assessments.models import Test, Question, Option

class Command(BaseCommand):
    help = "Seed Integrated Intelligence & Personality Assessment"

    def handle(self, *args, **kwargs):

        # ──────────────────────────────
        # 🧪 CREATE TEST
        # ──────────────────────────────
        test, created = Test.objects.get_or_create(
            slug="integrated-assessment",
            defaults={
                "name": "Integrated Intelligence & Personality Assessment",
                "description": "A unified psychometric test evaluating cognitive, emotional, behavioral and personality traits.",
                "category": "behavioral",
                "test_type": "scenario",
                "time_limit_mins": 20,
                "is_mandatory": False,
                "order": 2,
                "applicable_levels": ["10", "12", "undergraduate"]
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING("Test already exists. Skipping..."))
            return

        # ──────────────────────────────
        # 🧠 QUESTIONS
        # ──────────────────────────────

        questions_data = [

            # Q1
            {
                "text": "You are leading a project with a tight deadline. One team member is underperforming due to personal issues. The manager expects results without delay. What do you do?",
                "difficulty": "hard",
                "multiplier": 1.5,
                "options": [
                    ("Take over their work silently to ensure delivery", {"leadership": 0.7, "stress_tolerance": 0.9, "empathy": 0.4, "decision_making": 0.8}),
                    ("Talk privately, support them and redistribute tasks", {"empathy": 0.9, "leadership": 0.7, "communication": 0.8, "emotional_control": 0.8}),
                    ("Inform manager and request replacement", {"decision_making": 0.8, "assertiveness": 0.7, "risk_management": 0.9, "empathy": 0.3}),
                    ("Push the team harder without addressing the issue", {"leadership": 0.4, "empathy": 0.2, "stress_tolerance": 0.6}),
                ]
            },

            # Q2 (Cognitive + Logic)
            {
                "text": "A system processes 3 tasks per minute. Due to optimization, efficiency increases by 50%. How many tasks can it process in 4 minutes?",
                "difficulty": "medium",
                "multiplier": 1.2,
                "options": [
                    ("12", {"logical_reasoning": 0.2, "numerical_aptitude": 0.2}, False),
                    ("18", {"logical_reasoning": 1.0, "numerical_aptitude": 1.0}, True),
                    ("24", {"logical_reasoning": 0.5, "numerical_aptitude": 0.4}, False),
                    ("30", {"logical_reasoning": 0.3, "numerical_aptitude": 0.3}, False),
                ]
            },

            # Q3
            {
                "text": "You receive critical feedback in front of peers. How do you react?",
                "difficulty": "medium",
                "multiplier": 1.2,
                "options": [
                    ("Defend yourself immediately", {"emotional_control": 0.4, "assertiveness": 0.7}),
                    ("Stay calm, note feedback and reflect later", {"emotional_control": 0.9, "self_awareness": 0.8}),
                    ("Feel discouraged and disengage", {"emotional_control": 0.2, "resilience": 0.3}),
                    ("Challenge the feedback with logic", {"logical_reasoning": 0.8, "assertiveness": 0.8}),
                ]
            },

            # Q4
            {
                "text": "Your team has two conflicting ideas. Both seem viable. What is your approach?",
                "difficulty": "hard",
                "multiplier": 1.4,
                "options": [
                    ("Choose quickly based on instinct", {"decision_making": 0.6, "risk_taking": 0.7}),
                    ("Analyze both and combine best parts", {"problem_solving": 0.9, "creativity": 0.8}),
                    ("Let team vote", {"leadership": 0.6, "collaboration": 0.8}),
                    ("Escalate to senior authority", {"risk_management": 0.7, "decision_making": 0.5}),
                ]
            },

            # Q5
            {
                "text": "You notice a pattern anomaly in data others missed. What do you do?",
                "difficulty": "hard",
                "multiplier": 1.5,
                "options": [
                    ("Ignore assuming it's irrelevant", {"attention_to_detail": 0.2}),
                    ("Verify and report with evidence", {"analytical_thinking": 0.9, "attention_to_detail": 0.9}),
                    ("Quickly inform team without validation", {"communication": 0.7, "risk_management": 0.4}),
                    ("Deep dive extensively before sharing", {"analytical_thinking": 0.8, "perfectionism": 0.7}),
                ]
            },

            # Q6
            {
                "text": "Under high pressure, you are asked to make a decision with incomplete data.",
                "difficulty": "hard",
                "multiplier": 1.5,
                "options": [
                    ("Delay decision until more data arrives", {"risk_management": 0.8, "decision_making": 0.4}),
                    ("Make best possible decision with available data", {"decision_making": 0.9, "confidence": 0.8}),
                    ("Seek multiple opinions quickly", {"collaboration": 0.8, "communication": 0.7}),
                    ("Avoid responsibility", {"leadership": 0.1}),
                ]
            },

            # Q7
            {
                "text": "A colleague takes credit for your work. What do you do?",
                "difficulty": "medium",
                "multiplier": 1.3,
                "options": [
                    ("Confront publicly", {"assertiveness": 0.8, "emotional_control": 0.4}),
                    ("Discuss privately", {"communication": 0.9, "emotional_control": 0.8}),
                    ("Inform manager", {"decision_making": 0.7, "risk_management": 0.8}),
                    ("Ignore", {"emotional_control": 0.5, "assertiveness": 0.2}),
                ]
            },

            # Q8
            {
                "text": "You must learn a new skill quickly for a project.",
                "difficulty": "medium",
                "multiplier": 1.2,
                "options": [
                    ("Self-learn aggressively", {"learning_agility": 0.9, "discipline": 0.8}),
                    ("Take structured course", {"planning": 0.8, "discipline": 0.7}),
                    ("Ask others frequently", {"collaboration": 0.9}),
                    ("Avoid task", {"motivation": 0.1}),
                ]
            },

            # Q9
            {
                "text": "You are given ambiguous instructions for an important task.",
                "difficulty": "hard",
                "multiplier": 1.4,
                "options": [
                    ("Clarify immediately", {"communication": 0.9}),
                    ("Interpret and proceed", {"initiative": 0.8, "risk_taking": 0.7}),
                    ("Wait for clarity", {"risk_management": 0.7}),
                    ("Delegate to someone else", {"leadership": 0.3}),
                ]
            },

            # Q10
            {
                "text": "Which pattern completes the sequence: 2, 6, 12, 20, ?",
                "difficulty": "medium",
                "multiplier": 1.3,
                "options": [
                    ("30", {"logical_reasoning": 0.5}, False),
                    ("28", {"logical_reasoning": 1.0, "problem_solving": 1.0}, True),
                    ("26", {"logical_reasoning": 0.4}, False),
                    ("32", {"logical_reasoning": 0.3}, False),
                ]
            },
        ]

        # ──────────────────────────────
        # 💾 INSERT INTO DB
        # ──────────────────────────────

        for i, q in enumerate(questions_data, start=1):

            question = Question.objects.create(
                test=test,
                question_text=q["text"],
                question_type="scenario",
                difficulty=q["difficulty"],
                difficulty_multiplier=q["multiplier"],
                order=i
            )

            for j, opt in enumerate(q["options"], start=1):

                # Handle cognitive questions with correctness
                if len(opt) == 3:
                    text, scores, is_correct = opt
                else:
                    text, scores = opt
                    is_correct = False

                Option.objects.create(
                    question=question,
                    text=text,
                    scores=scores,
                    is_correct=is_correct,
                    order=j
                )

        self.stdout.write(self.style.SUCCESS("✅ Integrated Assessment Created Successfully!"))