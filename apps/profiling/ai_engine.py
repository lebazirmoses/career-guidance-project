import google.generativeai as genai
from django.conf import settings

def generate_personalized_roadmap(user, career):
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Role: Professional AI Career Advisor.
    User: {user.full_name}, current education: {user.profile.current_grade}, stream: {user.profile.stream}.
    Target Career: {career.name}.
    User Traits: {user.trait_vector.to_dict()}.
    
    Provide a specific 4-year roadmap for this student. 
    1. What subjects to focus on in {user.profile.stream}.
    2. Which 3 technical skills are most critical.
    3. The best UG/PG degree choice.
    4. A 1-sentence motivation 'Why this fits you'.
    Keep it structured with bullet points.
    """
    
    response = model.generate_content(prompt)
    return response.text