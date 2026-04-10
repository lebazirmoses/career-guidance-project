"""
Question Bank — Complete content for all test types.

Organization:
  COGNITIVE_QUESTIONS   → Timed logical, verbal, numerical
  BIG_FIVE_QUESTIONS    → MCQ personality (Big Five / OCEAN)
  RIASEC_QUESTIONS      → Scenario-based Holland Code
  EQ_QUESTIONS          → Emotional intelligence scenarios
  INTEREST_RANK_ITEMS   → Drag & rank interest areas
  FREE_TEXT_PROMPTS     → Open-ended AI-analyzed prompts

Each question has:
  - id
  - text
  - type
  - options (list)
  - correct_answer (where applicable)
  - trait_mapping (dict of trait → weight contribution)
  - difficulty (for cognitive)
  - applicable_levels (list of education level keys)
"""

ALL_LEVELS = [
    'middle_school', 'high_school', 'higher_sec',
    'undergraduate', 'postgraduate', 'working'
]
ADVANCED_LEVELS = ['undergraduate', 'postgraduate', 'working']
SCHOOL_LEVELS   = ['middle_school', 'high_school', 'higher_sec']


# ══════════════════════════════════════════════════════════════════════════════
# 1. COGNITIVE — LOGICAL REASONING (Timed, 30 sec/question)
# ══════════════════════════════════════════════════════════════════════════════

LOGICAL_QUESTIONS = [

    # ── Easy ──
    {
        "id": "LR001", "difficulty": "easy",
        "applicable_levels": ALL_LEVELS,
        "text": "Series: 2, 4, 8, 16, ___",
        "options": ["20", "24", "32", "28"],
        "correct_answer": "32",
        "trait_mapping": {"logical_reasoning": 0.7, "processing_speed": 0.3},
        "type": "timed"
    },
    {
        "id": "LR002", "difficulty": "easy",
        "applicable_levels": ALL_LEVELS,
        "text": "If all Roses are Flowers, and some Flowers are Red, then:",
        "options": [
            "All roses are red",
            "Some roses may be red",
            "No roses are red",
            "All flowers are roses"
        ],
        "correct_answer": "Some roses may be red",
        "trait_mapping": {"logical_reasoning": 0.8, "verbal_ability": 0.2},
        "type": "timed"
    },
    {
        "id": "LR003", "difficulty": "easy",
        "applicable_levels": ALL_LEVELS,
        "text": "Odd one out: [ Apple, Banana, Carrot, Mango ]",
        "options": ["Apple", "Banana", "Carrot", "Mango"],
        "correct_answer": "Carrot",
        "trait_mapping": {"logical_reasoning": 0.6, "verbal_ability": 0.4},
        "type": "timed"
    },

    # ── Medium ──
    {
        "id": "LR004", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "A clock shows 3:15. What is the angle between the hour and minute hands?",
        "options": ["0°", "7.5°", "15°", "30°"],
        "correct_answer": "7.5°",
        "trait_mapping": {"logical_reasoning": 0.7, "numerical_aptitude": 0.3},
        "type": "timed"
    },
    {
        "id": "LR005", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "Matrix: [ 1 2 / 3 4 ] → [ 2 4 / 6 8 ]. Same rule: [ 3 1 / 5 2 ] → ?",
        "options": ["[6 2 / 10 4]", "[3 2 / 5 4]", "[6 1 / 5 4]", "[4 2 / 6 3]"],
        "correct_answer": "[6 2 / 10 4]",
        "trait_mapping": {"logical_reasoning": 0.8, "spatial_reasoning": 0.2},
        "type": "timed"
    },
    {
        "id": "LR006", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "If FRIEND → HUMJTK, then CANDLE → ?",
        "options": ["FDQGOH", "ECOFJH", "FDPGOH", "ECQGJH"],
        "correct_answer": "FDQGOH",
        "trait_mapping": {"logical_reasoning": 0.6, "verbal_ability": 0.4},
        "type": "timed"
    },
    {
        "id": "LR007", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "5 people stand in a row. A is 2nd from left, C is 2nd from right. B is between A and C. Where is D if E is at the far right?",
        "options": ["1st from left", "Between B and C", "Far left", "4th from left"],
        "correct_answer": "Far left",
        "trait_mapping": {"logical_reasoning": 0.9, "spatial_reasoning": 0.1},
        "type": "timed"
    },

    # ── Hard ──
    {
        "id": "LR008", "difficulty": "hard",
        "applicable_levels": ADVANCED_LEVELS,
        "text": "A bat and a ball cost ₹110 total. The bat costs ₹100 more than the ball. How much does the ball cost?",
        "options": ["₹10", "₹5", "₹15", "₹20"],
        "correct_answer": "₹5",
        "trait_mapping": {"logical_reasoning": 0.6, "numerical_aptitude": 0.4},
        "type": "timed"
    },
    {
        "id": "LR009", "difficulty": "hard",
        "applicable_levels": ADVANCED_LEVELS,
        "text": "All P are Q. Some Q are R. No R is S. Which is definitely true?",
        "options": [
            "Some P are S",
            "Some Q are not S",
            "All Q are P",
            "No Q is S"
        ],
        "correct_answer": "Some Q are not S",
        "trait_mapping": {"logical_reasoning": 1.0},
        "type": "timed"
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# 2. COGNITIVE — VERBAL ABILITY (Timed, 25 sec/question)
# ══════════════════════════════════════════════════════════════════════════════

VERBAL_QUESTIONS = [
    {
        "id": "VA001", "difficulty": "easy",
        "applicable_levels": ALL_LEVELS,
        "text": "Choose the word most similar in meaning to: ABUNDANT",
        "options": ["Scarce", "Plentiful", "Average", "Hidden"],
        "correct_answer": "Plentiful",
        "trait_mapping": {"verbal_ability": 0.9, "logical_reasoning": 0.1},
        "type": "timed"
    },
    {
        "id": "VA002", "difficulty": "easy",
        "applicable_levels": ALL_LEVELS,
        "text": "Choose the correct sentence:",
        "options": [
            "She don't know the answer.",
            "She doesn't knows the answer.",
            "She doesn't know the answer.",
            "She not know the answer."
        ],
        "correct_answer": "She doesn't know the answer.",
        "trait_mapping": {"verbal_ability": 0.8, "attention_to_detail": 0.2},
        "type": "timed"
    },
    {
        "id": "VA003", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "DOCTOR : HOSPITAL :: TEACHER : ___",
        "options": ["Classroom", "School", "Book", "Student"],
        "correct_answer": "School",
        "trait_mapping": {"verbal_ability": 0.7, "logical_reasoning": 0.3},
        "type": "timed"
    },
    {
        "id": "VA004", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "Fill the blank: The scientist ________ her results three times before publishing.",
        "options": ["verify", "verifying", "verified", "verifies"],
        "correct_answer": "verified",
        "trait_mapping": {"verbal_ability": 1.0},
        "type": "timed"
    },
    {
        "id": "VA005", "difficulty": "hard",
        "applicable_levels": ADVANCED_LEVELS,
        "text": "Choose the word OPPOSITE in meaning to: EPHEMERAL",
        "options": ["Temporary", "Fleeting", "Permanent", "Fragile"],
        "correct_answer": "Permanent",
        "trait_mapping": {"verbal_ability": 0.9, "logical_reasoning": 0.1},
        "type": "timed"
    },
    {
        "id": "VA006", "difficulty": "hard",
        "applicable_levels": ADVANCED_LEVELS,
        "text": "Identify the logical flaw: 'Our product sales rose 30% after the ad campaign. Therefore, the campaign caused the increase.'",
        "options": [
            "False dilemma",
            "Post hoc ergo propter hoc (correlation ≠ causation)",
            "Ad hominem",
            "Slippery slope"
        ],
        "correct_answer": "Post hoc ergo propter hoc (correlation ≠ causation)",
        "trait_mapping": {"verbal_ability": 0.5, "logical_reasoning": 0.5},
        "type": "timed"
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# 3. COGNITIVE — NUMERICAL APTITUDE (Timed, 40 sec/question)
# ══════════════════════════════════════════════════════════════════════════════

NUMERICAL_QUESTIONS = [
    {
        "id": "NA001", "difficulty": "easy",
        "applicable_levels": ALL_LEVELS,
        "text": "A train travels 240 km in 4 hours. How long to travel 360 km at the same speed?",
        "options": ["5 hours", "6 hours", "7 hours", "4.5 hours"],
        "correct_answer": "6 hours",
        "trait_mapping": {"numerical_aptitude": 0.8, "logical_reasoning": 0.2},
        "type": "timed"
    },
    {
        "id": "NA002", "difficulty": "easy",
        "applicable_levels": ALL_LEVELS,
        "text": "What is 15% of 800?",
        "options": ["100", "110", "120", "130"],
        "correct_answer": "120",
        "trait_mapping": {"numerical_aptitude": 1.0},
        "type": "timed"
    },
    {
        "id": "NA003", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "A shopkeeper sells an item for ₹680 at a 15% profit. What was the cost price?",
        "options": ["₹580", "₹591.30", "₹600", "₹620"],
        "correct_answer": "₹591.30",
        "trait_mapping": {"numerical_aptitude": 0.9, "logical_reasoning": 0.1},
        "type": "timed"
    },
    {
        "id": "NA004", "difficulty": "medium",
        "applicable_levels": ALL_LEVELS,
        "text": "If x + y = 10 and xy = 24, what is x² + y²?",
        "options": ["52", "48", "64", "100"],
        "correct_answer": "52",
        "trait_mapping": {"numerical_aptitude": 0.7, "logical_reasoning": 0.3},
        "type": "timed"
    },
    {
        "id": "NA005", "difficulty": "hard",
        "applicable_levels": ADVANCED_LEVELS,
        "text": "Pipe A fills a tank in 6 hours, Pipe B in 8 hours. Pipe C empties it in 12 hours. All three open together — how long to fill?",
        "options": ["4.8 hrs", "5.0 hrs", "4.0 hrs", "6.0 hrs"],
        "correct_answer": "4.8 hrs",
        "trait_mapping": {"numerical_aptitude": 0.8, "logical_reasoning": 0.2},
        "type": "timed"
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# 4. PERSONALITY — BIG FIVE (MCQ, Untimed, 5-point Likert scale)
# ══════════════════════════════════════════════════════════════════════════════
# Options are always: Strongly Disagree / Disagree / Neutral / Agree / Strongly Agree
# Scores map 1–5, some reverse-scored (marked with reverse=True)

BIG_FIVE_QUESTIONS = [

    # ── Openness ──
    {
        "id": "BF001", "trait": "openness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I enjoy exploring new ideas and trying different approaches.",
        "type": "mcq",
        "trait_mapping": {"openness": 1.0}
    },
    {
        "id": "BF002", "trait": "openness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I am curious about how things work and why.",
        "type": "mcq",
        "trait_mapping": {"openness": 0.8, "investigative": 0.2}
    },
    {
        "id": "BF003", "trait": "openness", "reverse": True,
        "applicable_levels": ALL_LEVELS,
        "text": "I prefer doing things the tried-and-tested way.",
        "type": "mcq",
        "trait_mapping": {"openness": 1.0}
    },
    {
        "id": "BF004", "trait": "openness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I enjoy art, music, or literature even when it doesn't serve a practical purpose.",
        "type": "mcq",
        "trait_mapping": {"openness": 0.7, "artistic": 0.3}
    },

    # ── Conscientiousness ──
    {
        "id": "BF005", "trait": "conscientiousness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I complete tasks thoroughly and on time.",
        "type": "mcq",
        "trait_mapping": {"conscientiousness": 0.8, "attention_to_detail": 0.2}
    },
    {
        "id": "BF006", "trait": "conscientiousness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I make plans and stick to them.",
        "type": "mcq",
        "trait_mapping": {"conscientiousness": 1.0}
    },
    {
        "id": "BF007", "trait": "conscientiousness", "reverse": True,
        "applicable_levels": ALL_LEVELS,
        "text": "I often leave things to the last minute.",
        "type": "mcq",
        "trait_mapping": {"conscientiousness": 1.0}
    },
    {
        "id": "BF008", "trait": "conscientiousness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I pay close attention to details to avoid mistakes.",
        "type": "mcq",
        "trait_mapping": {"conscientiousness": 0.6, "attention_to_detail": 0.4}
    },

    # ── Extraversion ──
    {
        "id": "BF009", "trait": "extraversion", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I feel energized after spending time with a group of people.",
        "type": "mcq",
        "trait_mapping": {"extraversion": 0.8, "social": 0.2}
    },
    {
        "id": "BF010", "trait": "extraversion", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I enjoy being the center of attention at social gatherings.",
        "type": "mcq",
        "trait_mapping": {"extraversion": 0.7, "enterprising": 0.3}
    },
    {
        "id": "BF011", "trait": "extraversion", "reverse": True,
        "applicable_levels": ALL_LEVELS,
        "text": "I prefer quiet evenings at home to social events.",
        "type": "mcq",
        "trait_mapping": {"extraversion": 1.0}
    },
    {
        "id": "BF012", "trait": "extraversion", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I initiate conversations with new people easily.",
        "type": "mcq",
        "trait_mapping": {"extraversion": 0.6, "communication": 0.4}
    },

    # ── Agreeableness ──
    {
        "id": "BF013", "trait": "agreeableness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I find it easy to understand how others are feeling.",
        "type": "mcq",
        "trait_mapping": {"agreeableness": 0.6, "empathy": 0.4}
    },
    {
        "id": "BF014", "trait": "agreeableness", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I prioritize team harmony over winning an argument.",
        "type": "mcq",
        "trait_mapping": {"agreeableness": 0.7, "teamwork": 0.3}
    },
    {
        "id": "BF015", "trait": "agreeableness", "reverse": True,
        "applicable_levels": ALL_LEVELS,
        "text": "I can be tough and uncompromising when I need to be.",
        "type": "mcq",
        "trait_mapping": {"agreeableness": 1.0}
    },

    # ── Neuroticism ──
    {
        "id": "BF016", "trait": "neuroticism", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I get stressed easily when things don't go as planned.",
        "type": "mcq",
        "trait_mapping": {"neuroticism": 0.8, "resilience": -0.2}
    },
    {
        "id": "BF017", "trait": "neuroticism", "reverse": True,
        "applicable_levels": ALL_LEVELS,
        "text": "I remain calm even in high-pressure situations.",
        "type": "mcq",
        "trait_mapping": {"neuroticism": 0.7, "resilience": 0.3}
    },
    {
        "id": "BF018", "trait": "neuroticism", "reverse": False,
        "applicable_levels": ALL_LEVELS,
        "text": "I often worry about things that might go wrong.",
        "type": "mcq",
        "trait_mapping": {"neuroticism": 1.0}
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# 5. HOLLAND RIASEC — Scenario-Based
# ══════════════════════════════════════════════════════════════════════════════

RIASEC_QUESTIONS = [
    {
        "id": "RS001",
        "applicable_levels": ALL_LEVELS,
        "text": "You have a free Saturday. Which activity sounds most appealing?",
        "options": [
            "A. Build or repair something at home (machine, furniture, device)",
            "B. Research a topic that's been on your mind",
            "C. Write, draw, compose music, or make a video",
            "D. Volunteer at a community event or help a friend",
            "E. Organize a group outing or pitch a business idea",
            "F. Organize your files, budget, or plan the week ahead"
        ],
        "trait_mapping": {
            "A": {"realistic": 1.0},
            "B": {"investigative": 1.0},
            "C": {"artistic": 1.0},
            "D": {"social": 1.0},
            "E": {"enterprising": 1.0},
            "F": {"conventional": 1.0}
        },
        "type": "scenario"
    },
    {
        "id": "RS002",
        "applicable_levels": ALL_LEVELS,
        "text": "Your team is given an open-ended project. What role do you naturally take?",
        "options": [
            "A. Build the prototype or handle physical/technical setup",
            "B. Research and gather data to inform decisions",
            "C. Design the visual identity, story, or creative concept",
            "D. Facilitate the team, manage conflicts, support morale",
            "E. Lead the pitch, set goals, and keep everyone motivated",
            "F. Create the schedule, track progress, manage resources"
        ],
        "trait_mapping": {
            "A": {"realistic": 1.0},
            "B": {"investigative": 1.0},
            "C": {"artistic": 1.0},
            "D": {"social": 1.0},
            "E": {"enterprising": 1.0},
            "F": {"conventional": 1.0}
        },
        "type": "scenario"
    },
    {
        "id": "RS003",
        "applicable_levels": ALL_LEVELS,
        "text": "Which of these problems would you find most satisfying to solve?",
        "options": [
            "A. Fixing a broken machine or improving a mechanical system",
            "B. Figuring out why an experiment isn't working as expected",
            "C. Redesigning a product to make it more beautiful and intuitive",
            "D. Helping a struggling student finally understand something",
            "E. Convincing skeptical stakeholders to back a new idea",
            "F. Finding the error in a complex dataset or financial report"
        ],
        "trait_mapping": {
            "A": {"realistic": 1.0},
            "B": {"investigative": 1.0},
            "C": {"artistic": 1.0},
            "D": {"social": 1.0},
            "E": {"enterprising": 1.0},
            "F": {"conventional": 1.0}
        },
        "type": "scenario"
    },
    {
        "id": "RS004",
        "applicable_levels": ALL_LEVELS,
        "text": "Which workplace environment sounds most motivating to you?",
        "options": [
            "A. Outdoors, lab, workshop, or site — hands-on, physical",
            "B. A research lab or think tank with freedom to explore",
            "C. A creative studio — design agency, media house, or publisher",
            "D. A school, hospital, NGO, or counseling center",
            "E. A fast-moving startup or sales-driven company",
            "F. A structured office with clear systems and processes"
        ],
        "trait_mapping": {
            "A": {"realistic": 1.0},
            "B": {"investigative": 1.0},
            "C": {"artistic": 1.0},
            "D": {"social": 1.0},
            "E": {"enterprising": 1.0},
            "F": {"conventional": 1.0}
        },
        "type": "scenario"
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# 6. EMOTIONAL INTELLIGENCE — Scenario-Based
# ══════════════════════════════════════════════════════════════════════════════

EQ_QUESTIONS = [
    {
        "id": "EQ001",
        "applicable_levels": ALL_LEVELS,
        "text": "A close colleague snaps at you during a stressful project. Your first reaction is to:",
        "options": [
            "A. Snap back — they had no right to speak to you that way",
            "B. Walk away and cool down before addressing it",
            "C. Immediately ask if they're okay and what's wrong",
            "D. Ignore it and get back to work",
            "E. Report the behavior to a supervisor"
        ],
        "trait_mapping": {
            "A": {"empathy": -0.3, "neuroticism": 0.3},
            "B": {"resilience": 0.5, "empathy": 0.3},
            "C": {"empathy": 1.0, "social": 0.4},
            "D": {"neuroticism": 0.2, "attention_to_detail": 0.2},
            "E": {"conventional": 0.4}
        },
        "type": "scenario"
    },
    {
        "id": "EQ002",
        "applicable_levels": ALL_LEVELS,
        "text": "You receive harsh criticism on work you're proud of. You:",
        "options": [
            "A. Feel hurt and defensive, struggle to hear the feedback",
            "B. Take a breath, then extract what's useful from the criticism",
            "C. Ask clarifying questions to understand the reviewer's perspective",
            "D. Dismiss it — they don't understand your vision",
            "E. Immediately revise everything to please the reviewer"
        ],
        "trait_mapping": {
            "A": {"neuroticism": 0.5, "resilience": -0.2},
            "B": {"resilience": 0.8, "openness": 0.4},
            "C": {"empathy": 0.6, "openness": 0.4},
            "D": {"resilience": -0.3, "neuroticism": 0.2},
            "E": {"agreeableness": 0.4, "resilience": -0.1}
        },
        "type": "scenario"
    },
    {
        "id": "EQ003",
        "applicable_levels": ADVANCED_LEVELS,
        "text": "You notice a junior team member is consistently underperforming and seems disengaged. You:",
        "options": [
            "A. Report it to your manager — it's not your problem",
            "B. Have a private, non-judgmental conversation to understand what's happening",
            "C. Assign them easier work to reduce pressure",
            "D. Push them harder — pressure builds performance",
            "E. Publicly praise others in the team to motivate them indirectly"
        ],
        "trait_mapping": {
            "A": {"empathy": -0.3, "social": -0.2},
            "B": {"empathy": 1.0, "leadership": 0.6, "social": 0.4},
            "C": {"empathy": 0.4, "social": 0.3},
            "D": {"leadership": 0.2, "empathy": -0.4},
            "E": {"leadership": 0.1, "empathy": -0.2}
        },
        "type": "scenario"
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# 7. DRAG & RANK — Interest Areas
# ══════════════════════════════════════════════════════════════════════════════

INTEREST_RANK_SETS = [
    {
        "id": "DR001",
        "applicable_levels": ALL_LEVELS,
        "instruction": "Drag to rank these areas from MOST interesting (top) to LEAST interesting (bottom).",
        "items": [
            "Technology & Computers",
            "Human Body & Medicine",
            "Business & Money",
            "Art, Design & Creativity",
            "Nature & Environment",
            "Law & Justice",
            "Teaching & Education",
            "Sports & Fitness",
            "Music & Performing Arts",
            "Research & Science"
        ],
        "trait_mapping_by_rank": {
            "Technology & Computers": {"investigative": 0.4, "realistic": 0.3, "logical_reasoning": 0.3},
            "Human Body & Medicine": {"investigative": 0.4, "social": 0.4, "empathy": 0.2},
            "Business & Money": {"enterprising": 0.6, "numerical_aptitude": 0.4},
            "Art, Design & Creativity": {"artistic": 0.8, "openness": 0.2},
            "Nature & Environment": {"realistic": 0.5, "investigative": 0.3, "social_impact_drive": 0.2},
            "Law & Justice": {"enterprising": 0.4, "social": 0.4, "verbal_ability": 0.2},
            "Teaching & Education": {"social": 0.7, "empathy": 0.3},
            "Sports & Fitness": {"realistic": 0.6, "resilience": 0.4},
            "Music & Performing Arts": {"artistic": 0.7, "extraversion": 0.3},
            "Research & Science": {"investigative": 0.8, "logical_reasoning": 0.2}
        },
        "type": "drag_rank"
    },
    {
        "id": "DR002",
        "applicable_levels": ALL_LEVELS,
        "instruction": "Rank these work VALUES from most important to you (top) to least (bottom).",
        "items": [
            "High salary & financial reward",
            "Making a difference in society",
            "Creative freedom & self-expression",
            "Job security & stability",
            "Fame, recognition & status",
            "Learning & intellectual growth",
            "Work-life balance",
            "Leadership & influence",
            "Teamwork & belonging",
            "Autonomy & independence"
        ],
        "trait_mapping_by_rank": {
            "High salary & financial reward":        {"extrinsic_motivation": 0.8, "enterprising": 0.2},
            "Making a difference in society":        {"social_impact_drive": 0.8, "intrinsic_motivation": 0.2},
            "Creative freedom & self-expression":    {"artistic": 0.6, "autonomy_preference": 0.4},
            "Job security & stability":              {"conventional": 0.6, "neuroticism": 0.4},
            "Fame, recognition & status":            {"extrinsic_motivation": 0.7, "enterprising": 0.3},
            "Learning & intellectual growth":        {"intrinsic_motivation": 0.8, "investigative": 0.2},
            "Work-life balance":                     {"autonomy_preference": 0.6, "neuroticism": 0.4},
            "Leadership & influence":                {"leadership": 0.7, "enterprising": 0.3},
            "Teamwork & belonging":                  {"social": 0.6, "agreeableness": 0.4},
            "Autonomy & independence":               {"autonomy_preference": 0.8, "realistic": 0.2}
        },
        "type": "drag_rank"
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# 8. FREE TEXT — Open-ended, AI-analyzed prompts
# ══════════════════════════════════════════════════════════════════════════════

FREE_TEXT_PROMPTS = [
    {
        "id": "FT001",
        "applicable_levels": ALL_LEVELS,
        "prompt": "Describe yourself in 3–5 sentences. Who are you, what do you care about, and what makes you different from others your age?",
        "ai_analysis_target": ["openness", "extraversion", "intrinsic_motivation", "social_impact_drive"],
        "type": "free_text",
        "min_words": 30,
        "max_words": 200
    },
    {
        "id": "FT002",
        "applicable_levels": ALL_LEVELS,
        "prompt": "Tell us about something you built, created, solved, or achieved that you're genuinely proud of. What was it, and what did you learn from it?",
        "ai_analysis_target": ["creativity", "resilience", "conscientiousness", "intrinsic_motivation"],
        "type": "free_text",
        "min_words": 40,
        "max_words": 250
    },
    {
        "id": "FT003",
        "applicable_levels": ALL_LEVELS,
        "prompt": "Describe your ideal working day 10 years from now. Where are you, what are you doing, and who are you doing it with?",
        "ai_analysis_target": ["autonomy_preference", "social", "enterprising", "realistic", "artistic"],
        "type": "free_text",
        "min_words": 40,
        "max_words": 250
    },
    {
        "id": "FT004",
        "applicable_levels": ADVANCED_LEVELS,
        "prompt": "Describe a time you failed at something important. What happened, and how did you respond? What did it teach you?",
        "ai_analysis_target": ["resilience", "neuroticism", "openness", "conscientiousness"],
        "type": "free_text",
        "min_words": 50,
        "max_words": 300
    },
]