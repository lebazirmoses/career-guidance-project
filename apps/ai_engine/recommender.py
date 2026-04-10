import math
from apps.jobs.models import Career

def get_recommendations(user_vector):
    user_traits = user_vector.to_dict()
    careers = Career.objects.all()
    recommendations = []

    for career in careers:
        # Simple Euclidean Distance: Lower is better
        # distance = sqrt(sum((user_trait - career_trait)^2))
        score = 0
        score += (user_traits.get('logical_reasoning', 0) - career.required_logic)**2
        score += (user_traits.get('creativity', 0) - career.required_creativity)**2
        # ... add other traits ...
        
        final_distance = math.sqrt(score)
        
        # Convert distance to a "Match Percentage"
        match_percentage = max(0, 100 - (final_distance * 100))
        
        recommendations.append({
            'career': career,
            'match': match_percentage
        })

    # Sort by highest match
    return sorted(recommendations, key=lambda x: x['match'], reverse=True)[:3]