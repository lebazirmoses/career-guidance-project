import json
import os
from django.core.management.base import BaseCommand
from apps.assessments.models import Test, Question, Option


class Command(BaseCommand):
    help = "Load assessment tests from JSON files"

    def handle(self, *args, **kwargs):
        base_path = "apps/assessments/data"

        for file in os.listdir(base_path):
            if file.endswith(".json"):
                full_path = os.path.join(base_path, file)

                with open(full_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                test, created = Test.objects.get_or_create(
                    slug=data["slug"],
                    defaults={
                        "name": data["name"],
                        "description": data.get("description", ""),
                        "category": data["category"],
                        "test_type": data["test_type"],
                        "time_limit_mins": data.get("time_limit_mins"),
                        "is_mandatory": data.get("is_mandatory", False),
                        "applicable_levels": data.get("applicable_levels", []),
                    }
                )

                if not created:
                    # Update existing test
                    test.name = data["name"]
                    test.description = data.get("description", "")
                    test.category = data["category"]
                    test.test_type = data["test_type"]
                    test.time_limit_mins = data.get("time_limit_mins")
                    test.is_mandatory = data.get("is_mandatory", False)
                    test.applicable_levels = data.get("applicable_levels", [])
                    test.save()

                self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} Test: {test.name}"))

                # 🔥 CLEAR OLD DATA
                test.questions.all().delete()

                # 🔥 CREATE QUESTIONS + OPTIONS
                for i, q in enumerate(data["questions"], start=1):

                    question = Question.objects.create(
                        test=test,
                        question_text=q["text"],
                        question_type=data["test_type"],
                        difficulty_multiplier=q.get("difficulty_multiplier", 1.0),
                        order=i,
                    )

                    # ✅ CREATE OPTIONS PROPERLY
                    for j, opt in enumerate(q.get("options", []), start=1):
                        Option.objects.create(
                            question=question,
                            text=opt["text"],
                            scores=opt.get("scores", {}),
                            is_correct=opt.get("is_correct", False),
                            order=j,
                        )

                self.stdout.write(
                    self.style.SUCCESS(f"Loaded {len(data['questions'])} questions")
                )