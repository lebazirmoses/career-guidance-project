import os
import json
import django
import sys

# Add project root to sys.path to allow imports
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.assessments.models import Test, Question

def run_seeder():
    file_path = os.path.join('data', 'master_questions.json')
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        questions_data = json.load(f)

    count = 0
    for q in questions_data:
        # Create or Get the Test category
        test, _ = Test.objects.get_or_create(
            slug=q['test_slug'],
            defaults={
                'name': q['test_slug'].replace('-', ' ').title(),
                'category': 'personality' if 'personality' in q['test_slug'] else 'cognitive',
                'applicable_levels': ["UG", "12th", "10th"]
            }
        )

        # Create the Question
        Question.objects.get_or_create(
            test=test,
            question_text=q['question_text'],
            defaults={
                'question_type': q['type'],
                'options': q['options'],
                'correct_answer': q.get('correct_answer', ''),
                'trait_mapping': q['trait_mapping']
            }
        )
        count += 1

    print(f"✅ Intelligence Engine Loaded: {count} questions added/verified.")

if __name__ == "__main__":
    run_seeder()