# management/commands/load_careers.py

import json
from django.core.management.base import BaseCommand
from apps.dashboard.models import CareerNode

class Command(BaseCommand):
    help = "Load clean career dataset"

    def handle(self, *args, **kwargs):

        with open("career_dataset.json", encoding="utf-8") as f:
            data = json.load(f)

        node_map = {}

        # STEP 1: Create unique nodes
        for item in data:
            name = item["name"].strip()
            stage = item["stage"]

            key = (name, stage)

            if key not in node_map:
                node, _ = CareerNode.objects.get_or_create(
                    name=name,
                    defaults={"stage": stage}
                )
                node_map[key] = node

        # STEP 2: Assign parents safely
        for item in data:
            name = item["name"].strip()
            parent_name = item.get("parent")

            node = CareerNode.objects.filter(name=name).first()

            if parent_name:
                parent = CareerNode.objects.filter(name=parent_name).first()
                if parent and node and node.parent != parent:
                    node.parent = parent
                    node.save()

        self.stdout.write(self.style.SUCCESS("✅ Clean dataset loaded!"))