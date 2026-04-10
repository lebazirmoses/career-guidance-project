# apps/assessments/management/commands/seed_career.py
import json
from django.core.management.base import BaseCommand
from apps.dashboard.utils import seed_career_tree

class Command(BaseCommand):
    help = "Seeds the career tree from JSON"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding career tree...")
        with open('apps/dashboard/data/career_path.json', 'r', encoding='utf-8') as f:
            nested_data = json.load(f)

        seed_career_tree(nested_data)
        self.stdout.write(self.style.SUCCESS("Career tree seeded successfully!"))