"""
Profession Database — Indian context, comprehensive.

Each profession has:
  - id, name, category, description
  - required_traits: dict of trait → minimum score (0–1)
  - ideal_traits: dict of trait → ideal score (used for fit % calc)
  - riasec_code: primary Holland codes (e.g. "ISE")
  - indian_pathways: list of pathway IDs from indian_pathways.py
  - education_min: minimum education level required
  - market_demand: 1 (low) – 5 (high) in Indian market
  - salary_range_lpa: [min, max] in Lakhs Per Annum (Indian context)
  - tags: searchable keywords
"""

PROFESSIONS = [

    # ══════════════════════════════════════════════════════════
    # TECHNOLOGY & COMPUTING
    # ══════════════════════════════════════════════════════════

    {
        "id": "TECH001",
        "name": "Software Engineer",
        "category": "Technology",
        "description": "Design, build, and maintain software systems and applications.",
        "required_traits": {
            "logical_reasoning": 0.65,
            "numerical_aptitude": 0.50,
            "attention_to_detail": 0.60,
        },
        "ideal_traits": {
            "logical_reasoning": 0.85,
            "numerical_aptitude": 0.70,
            "conscientiousness": 0.75,
            "openness": 0.65,
            "attention_to_detail": 0.80,
            "investigative": 0.70,
        },
        "riasec_code": "IRC",
        "education_min": "higher_sec",
        "market_demand": 5,
        "salary_range_lpa": [5, 50],
        "tags": ["coding", "programming", "developer", "software", "IT"]
    },
    {
        "id": "TECH002",
        "name": "Data Scientist",
        "category": "Technology",
        "description": "Extract insights from complex data using statistics, ML, and AI.",
        "required_traits": {
            "logical_reasoning": 0.75,
            "numerical_aptitude": 0.75,
            "investigative": 0.65,
        },
        "ideal_traits": {
            "logical_reasoning": 0.90,
            "numerical_aptitude": 0.85,
            "investigative": 0.80,
            "conscientiousness": 0.70,
            "openness": 0.70,
            "attention_to_detail": 0.75,
        },
        "riasec_code": "IRA",
        "education_min": "undergraduate",
        "market_demand": 5,
        "salary_range_lpa": [8, 60],
        "tags": ["data", "machine learning", "AI", "statistics", "analytics"]
    },
    {
        "id": "TECH003",
        "name": "UX/UI Designer",
        "category": "Technology",
        "description": "Design user interfaces and experiences for digital products.",
        "required_traits": {
            "artistic": 0.65,
            "empathy": 0.60,
        },
        "ideal_traits": {
            "artistic": 0.85,
            "empathy": 0.75,
            "openness": 0.80,
            "investigative": 0.55,
            "attention_to_detail": 0.70,
        },
        "riasec_code": "AIS",
        "education_min": "higher_sec",
        "market_demand": 4,
        "salary_range_lpa": [4, 35],
        "tags": ["design", "UI", "UX", "figma", "user experience", "creative"]
    },
    {
        "id": "TECH004",
        "name": "Cybersecurity Analyst",
        "category": "Technology",
        "description": "Protect systems, networks, and data from cyber threats.",
        "required_traits": {
            "logical_reasoning": 0.70,
            "attention_to_detail": 0.75,
        },
        "ideal_traits": {
            "logical_reasoning": 0.85,
            "attention_to_detail": 0.90,
            "conscientiousness": 0.80,
            "investigative": 0.70,
            "resilience": 0.65,
        },
        "riasec_code": "IRC",
        "education_min": "undergraduate",
        "market_demand": 5,
        "salary_range_lpa": [6, 40],
        "tags": ["security", "ethical hacking", "networking", "cyber"]
    },
    {
        "id": "TECH005",
        "name": "AI/ML Engineer",
        "category": "Technology",
        "description": "Build and deploy machine learning models and AI systems.",
        "required_traits": {
            "logical_reasoning": 0.80,
            "numerical_aptitude": 0.75,
            "investigative": 0.70,
        },
        "ideal_traits": {
            "logical_reasoning": 0.92,
            "numerical_aptitude": 0.88,
            "investigative": 0.82,
            "openness": 0.72,
            "conscientiousness": 0.75,
        },
        "riasec_code": "IRA",
        "education_min": "undergraduate",
        "market_demand": 5,
        "salary_range_lpa": [10, 80],
        "tags": ["AI", "machine learning", "deep learning", "neural networks"]
    },
    {
        "id": "TECH006",
        "name": "Product Manager",
        "category": "Technology",
        "description": "Define product vision, strategy, and roadmap; bridge tech and business.",
        "required_traits": {
            "leadership": 0.65,
            "communication": 0.70,
            "logical_reasoning": 0.60,
        },
        "ideal_traits": {
            "leadership": 0.80,
            "communication": 0.85,
            "empathy": 0.75,
            "enterprising": 0.75,
            "logical_reasoning": 0.70,
            "openness": 0.70,
        },
        "riasec_code": "EIS",
        "education_min": "undergraduate",
        "market_demand": 5,
        "salary_range_lpa": [12, 70],
        "tags": ["product", "PM", "strategy", "roadmap", "startup"]
    },

    # ══════════════════════════════════════════════════════════
    # MEDICINE & HEALTHCARE
    # ══════════════════════════════════════════════════════════

    {
        "id": "MED001",
        "name": "Medical Doctor (MBBS/MD)",
        "category": "Healthcare",
        "description": "Diagnose and treat patients; specialize in various medical disciplines.",
        "required_traits": {
            "logical_reasoning": 0.70,
            "empathy": 0.70,
            "attention_to_detail": 0.80,
            "resilience": 0.65,
        },
        "ideal_traits": {
            "logical_reasoning": 0.85,
            "empathy": 0.85,
            "attention_to_detail": 0.90,
            "resilience": 0.80,
            "conscientiousness": 0.85,
            "investigative": 0.70,
            "social": 0.75,
        },
        "riasec_code": "ISR",
        "education_min": "higher_sec",
        "market_demand": 5,
        "salary_range_lpa": [8, 100],
        "tags": ["doctor", "MBBS", "medicine", "hospital", "clinical"]
    },
    {
        "id": "MED002",
        "name": "Psychologist / Counselor",
        "category": "Healthcare",
        "description": "Study human behavior; provide therapy, counseling, and mental health support.",
        "required_traits": {
            "empathy": 0.80,
            "social": 0.70,
            "verbal_ability": 0.65,
        },
        "ideal_traits": {
            "empathy": 0.90,
            "social": 0.85,
            "verbal_ability": 0.75,
            "agreeableness": 0.80,
            "openness": 0.70,
            "investigative": 0.65,
        },
        "riasec_code": "SIA",
        "education_min": "undergraduate",
        "market_demand": 4,
        "salary_range_lpa": [4, 25],
        "tags": ["psychology", "counseling", "mental health", "therapy"]
    },
    {
        "id": "MED003",
        "name": "Biomedical Engineer",
        "category": "Healthcare",
        "description": "Design medical devices and equipment; bridge engineering with medicine.",
        "required_traits": {
            "logical_reasoning": 0.70,
            "numerical_aptitude": 0.65,
            "investigative": 0.60,
        },
        "ideal_traits": {
            "logical_reasoning": 0.82,
            "numerical_aptitude": 0.78,
            "investigative": 0.75,
            "realistic": 0.65,
            "conscientiousness": 0.72,
        },
        "riasec_code": "IRE",
        "education_min": "undergraduate",
        "market_demand": 3,
        "salary_range_lpa": [4, 20],
        "tags": ["biomedical", "medical devices", "engineering", "healthcare tech"]
    },

    # ══════════════════════════════════════════════════════════
    # BUSINESS & FINANCE
    # ══════════════════════════════════════════════════════════

    {
        "id": "BIZ001",
        "name": "Chartered Accountant (CA)",
        "category": "Finance",
        "description": "Financial reporting, auditing, tax planning, and accounting.",
        "required_traits": {
            "numerical_aptitude": 0.80,
            "attention_to_detail": 0.85,
            "conscientiousness": 0.80,
        },
        "ideal_traits": {
            "numerical_aptitude": 0.90,
            "attention_to_detail": 0.92,
            "conscientiousness": 0.88,
            "conventional": 0.80,
            "logical_reasoning": 0.72,
        },
        "riasec_code": "CEI",
        "education_min": "higher_sec",
        "market_demand": 5,
        "salary_range_lpa": [7, 60],
        "tags": ["CA", "accounting", "finance", "audit", "tax", "ICAI"]
    },
    {
        "id": "BIZ002",
        "name": "Entrepreneur / Startup Founder",
        "category": "Business",
        "description": "Build and scale a business from an idea; manage risk, teams, and growth.",
        "required_traits": {
            "risk_appetite": 0.70,
            "resilience": 0.75,
            "leadership": 0.65,
        },
        "ideal_traits": {
            "risk_appetite": 0.85,
            "resilience": 0.90,
            "leadership": 0.82,
            "enterprising": 0.85,
            "creativity": 0.75,
            "communication": 0.78,
            "intrinsic_motivation": 0.85,
        },
        "riasec_code": "EAI",
        "education_min": "high_school",
        "market_demand": 4,
        "salary_range_lpa": [0, 500],
        "tags": ["entrepreneur", "startup", "founder", "business", "self-employed"]
    },
    {
        "id": "BIZ003",
        "name": "Management Consultant",
        "category": "Business",
        "description": "Advise organizations on strategy, operations, and problem-solving.",
        "required_traits": {
            "logical_reasoning": 0.75,
            "communication": 0.75,
            "leadership": 0.60,
        },
        "ideal_traits": {
            "logical_reasoning": 0.88,
            "communication": 0.88,
            "leadership": 0.75,
            "enterprising": 0.78,
            "verbal_ability": 0.80,
            "resilience": 0.70,
        },
        "riasec_code": "EIC",
        "education_min": "undergraduate",
        "market_demand": 4,
        "salary_range_lpa": [12, 80],
        "tags": ["consulting", "McKinsey", "strategy", "MBA", "business analyst"]
    },

    # ══════════════════════════════════════════════════════════
    # CREATIVE & ARTS
    # ══════════════════════════════════════════════════════════

    {
        "id": "ART001",
        "name": "Graphic Designer",
        "category": "Creative",
        "description": "Create visual content for communication — branding, print, digital.",
        "required_traits": {
            "artistic": 0.75,
            "creativity": 0.70,
        },
        "ideal_traits": {
            "artistic": 0.90,
            "creativity": 0.85,
            "openness": 0.80,
            "attention_to_detail": 0.70,
            "conscientiousness": 0.65,
        },
        "riasec_code": "ARC",
        "education_min": "higher_sec",
        "market_demand": 4,
        "salary_range_lpa": [2.5, 20],
        "tags": ["graphic design", "visual", "branding", "illustrator", "photoshop"]
    },
    {
        "id": "ART002",
        "name": "Filmmaker / Cinematographer",
        "category": "Creative",
        "description": "Direct, shoot, and edit films, documentaries, or video content.",
        "required_traits": {
            "artistic": 0.75,
            "creativity": 0.75,
        },
        "ideal_traits": {
            "artistic": 0.90,
            "creativity": 0.88,
            "leadership": 0.65,
            "openness": 0.85,
            "communication": 0.70,
        },
        "riasec_code": "AES",
        "education_min": "higher_sec",
        "market_demand": 3,
        "salary_range_lpa": [2, 30],
        "tags": ["film", "cinema", "director", "cinematography", "media"]
    },

    # ══════════════════════════════════════════════════════════
    # EDUCATION & RESEARCH
    # ══════════════════════════════════════════════════════════

    {
        "id": "EDU001",
        "name": "Teacher / Educator",
        "category": "Education",
        "description": "Educate students at school or university level in a subject domain.",
        "required_traits": {
            "social": 0.70,
            "communication": 0.70,
            "empathy": 0.65,
        },
        "ideal_traits": {
            "social": 0.85,
            "communication": 0.85,
            "empathy": 0.80,
            "conscientiousness": 0.75,
            "openness": 0.65,
            "intrinsic_motivation": 0.75,
        },
        "riasec_code": "SAI",
        "education_min": "undergraduate",
        "market_demand": 4,
        "salary_range_lpa": [3, 20],
        "tags": ["teaching", "school", "education", "professor", "lecturer"]
    },
    {
        "id": "EDU002",
        "name": "Research Scientist",
        "category": "Research",
        "description": "Conduct original research to advance knowledge in a scientific field.",
        "required_traits": {
            "investigative": 0.80,
            "logical_reasoning": 0.75,
            "conscientiousness": 0.75,
        },
        "ideal_traits": {
            "investigative": 0.92,
            "logical_reasoning": 0.88,
            "conscientiousness": 0.85,
            "openness": 0.80,
            "attention_to_detail": 0.85,
            "intrinsic_motivation": 0.88,
        },
        "riasec_code": "IRA",
        "education_min": "postgraduate",
        "market_demand": 3,
        "salary_range_lpa": [5, 30],
        "tags": ["research", "PhD", "scientist", "laboratory", "academia"]
    },

    # ══════════════════════════════════════════════════════════
    # LAW & GOVERNANCE
    # ══════════════════════════════════════════════════════════

    {
        "id": "LAW001",
        "name": "Advocate / Lawyer",
        "category": "Law",
        "description": "Represent clients in legal matters; advise on rights and obligations.",
        "required_traits": {
            "verbal_ability": 0.80,
            "logical_reasoning": 0.70,
            "communication": 0.75,
        },
        "ideal_traits": {
            "verbal_ability": 0.90,
            "logical_reasoning": 0.82,
            "communication": 0.88,
            "enterprising": 0.72,
            "conscientiousness": 0.78,
            "resilience": 0.72,
        },
        "riasec_code": "EIS",
        "education_min": "undergraduate",
        "market_demand": 4,
        "salary_range_lpa": [4, 80],
        "tags": ["law", "advocate", "legal", "court", "LLB", "litigation"]
    },
    {
        "id": "LAW002",
        "name": "Civil Services Officer (IAS/IPS/IFS)",
        "category": "Government",
        "description": "Administer public services, policy, and governance across India.",
        "required_traits": {
            "logical_reasoning": 0.80,
            "verbal_ability": 0.75,
            "resilience": 0.80,
            "conscientiousness": 0.80,
        },
        "ideal_traits": {
            "logical_reasoning": 0.90,
            "verbal_ability": 0.88,
            "resilience": 0.88,
            "conscientiousness": 0.90,
            "social_impact_drive": 0.85,
            "leadership": 0.78,
        },
        "riasec_code": "ESC",
        "education_min": "undergraduate",
        "market_demand": 5,
        "salary_range_lpa": [7, 20],
        "tags": ["IAS", "IPS", "UPSC", "civil services", "government", "bureaucracy"]
    },

    # ══════════════════════════════════════════════════════════
    # ENGINEERING (non-software)
    # ══════════════════════════════════════════════════════════

    {
        "id": "ENG001",
        "name": "Mechanical Engineer",
        "category": "Engineering",
        "description": "Design, build, and maintain mechanical systems and machinery.",
        "required_traits": {
            "logical_reasoning": 0.65,
            "numerical_aptitude": 0.65,
            "realistic": 0.65,
        },
        "ideal_traits": {
            "logical_reasoning": 0.80,
            "numerical_aptitude": 0.78,
            "realistic": 0.78,
            "spatial_reasoning": 0.75,
            "attention_to_detail": 0.72,
            "conscientiousness": 0.70,
        },
        "riasec_code": "RIC",
        "education_min": "undergraduate",
        "market_demand": 3,
        "salary_range_lpa": [3, 25],
        "tags": ["mechanical", "engineering", "manufacturing", "CAD", "machines"]
    },
    {
        "id": "ENG002",
        "name": "Civil Engineer",
        "category": "Engineering",
        "description": "Plan, design, and oversee construction of infrastructure.",
        "required_traits": {
            "logical_reasoning": 0.65,
            "numerical_aptitude": 0.65,
            "realistic": 0.60,
        },
        "ideal_traits": {
            "logical_reasoning": 0.78,
            "numerical_aptitude": 0.75,
            "realistic": 0.80,
            "spatial_reasoning": 0.72,
            "conscientiousness": 0.75,
        },
        "riasec_code": "RIC",
        "education_min": "undergraduate",
        "market_demand": 3,
        "salary_range_lpa": [3, 20],
        "tags": ["civil", "construction", "infrastructure", "buildings", "roads"]
    },

    # ══════════════════════════════════════════════════════════
    # MEDIA & COMMUNICATION
    # ══════════════════════════════════════════════════════════

    {
        "id": "MED010",
        "name": "Journalist / Content Creator",
        "category": "Media",
        "description": "Research, write, and present stories across print, digital, or broadcast.",
        "required_traits": {
            "verbal_ability": 0.75,
            "communication": 0.70,
            "openness": 0.65,
        },
        "ideal_traits": {
            "verbal_ability": 0.88,
            "communication": 0.85,
            "openness": 0.80,
            "investigative": 0.70,
            "artistic": 0.65,
            "resilience": 0.65,
        },
        "riasec_code": "AEI",
        "education_min": "higher_sec",
        "market_demand": 3,
        "salary_range_lpa": [2.5, 25],
        "tags": ["journalism", "writing", "content", "media", "reporter", "blogger"]
    },

    # ══════════════════════════════════════════════════════════
    # DEFENCE & UNIFORMED SERVICES
    # ══════════════════════════════════════════════════════════

    {
        "id": "DEF001",
        "name": "Armed Forces Officer (Army/Navy/Air Force)",
        "category": "Defence",
        "description": "Lead and serve in India's armed forces; roles in combat, logistics, and strategy.",
        "required_traits": {
            "resilience": 0.85,
            "leadership": 0.70,
            "conscientiousness": 0.75,
        },
        "ideal_traits": {
            "resilience": 0.92,
            "leadership": 0.85,
            "conscientiousness": 0.88,
            "teamwork": 0.82,
            "logical_reasoning": 0.70,
            "social_impact_drive": 0.75,
        },
        "riasec_code": "RES",
        "education_min": "higher_sec",
        "market_demand": 4,
        "salary_range_lpa": [6, 25],
        "tags": ["army", "navy", "airforce", "NDA", "CDS", "defence", "military"]
    },

    # ══════════════════════════════════════════════════════════
    # SOCIAL IMPACT & NGO
    # ══════════════════════════════════════════════════════════

    {
        "id": "SOC001",
        "name": "Social Worker / Development Professional",
        "category": "Social Impact",
        "description": "Work with communities, NGOs, or government on social development programs.",
        "required_traits": {
            "empathy": 0.80,
            "social": 0.75,
            "social_impact_drive": 0.75,
        },
        "ideal_traits": {
            "empathy": 0.90,
            "social": 0.88,
            "social_impact_drive": 0.90,
            "resilience": 0.72,
            "communication": 0.75,
            "agreeableness": 0.80,
        },
        "riasec_code": "SAE",
        "education_min": "undergraduate",
        "market_demand": 3,
        "salary_range_lpa": [2.5, 15],
        "tags": ["NGO", "social work", "development", "community", "non-profit"]
    },
]