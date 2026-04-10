"""
Indian Education Pathway Map — Stage-by-stage routes to each profession.

Structure:
  Each pathway is a list of stages.
  Each stage has:
    - level: education level key
    - title: what to do at this level
    - options: list of specific paths (streams, boards, exams, colleges)
    - duration: time at this stage
    - notes: important context for Indian students
"""

PATHWAYS = {

    "path_software_engineer": {
        "target_professions": ["TECH001", "TECH002", "TECH005"],
        "stages": [
            {
                "level": "high_school",
                "title": "Choose the right stream in 9th–10th",
                "options": [
                    "Science stream with Maths — essential",
                    "Focus on Maths & Computer Science if available",
                ],
                "duration": "2 years",
                "notes": "Score above 85% for top engineering college admission"
            },
            {
                "level": "higher_sec",
                "title": "11th–12th: Science with Computer Science",
                "options": [
                    "CBSE: PCM + Computer Science",
                    "State Board: Maths, Physics, Chemistry + CS elective",
                    "Prepare for JEE Main / JEE Advanced / BITSAT",
                ],
                "duration": "2 years",
                "notes": "JEE rank determines IIT/NIT/BITS. State board score for state engineering colleges."
            },
            {
                "level": "undergraduate",
                "title": "B.Tech / B.E. in Computer Science or related",
                "options": [
                    "IITs (via JEE Advanced) — top choice",
                    "NITs (via JEE Main)",
                    "BITS Pilani (via BITSAT)",
                    "State Government Engineering Colleges",
                    "Private: VIT, SRM, Manipal, Amity etc.",
                    "B.Sc Computer Science (3 year option)",
                ],
                "duration": "4 years",
                "notes": "Internships, competitive programming, open-source contribution crucial. CGPA matters for campus placements."
            },
            {
                "level": "postgraduate",
                "title": "Optional: M.Tech / MS / MBA",
                "options": [
                    "M.Tech at IIT/NIT (via GATE) — for R&D / academia",
                    "MS in USA/Canada/Europe — for global exposure",
                    "MBA — to move into product/management roles",
                ],
                "duration": "2 years",
                "notes": "Most software engineers go directly to industry after B.Tech."
            }
        ]
    },

    "path_doctor": {
        "target_professions": ["MED001"],
        "stages": [
            {
                "level": "high_school",
                "title": "9th–10th: Science with Biology focus",
                "options": [
                    "Science stream with Biology — mandatory",
                    "Strong focus on Biology, Chemistry, Physics",
                ],
                "duration": "2 years",
                "notes": "Board marks matter less than NEET score, but a strong foundation helps."
            },
            {
                "level": "higher_sec",
                "title": "11th–12th: Science (PCB) + NEET Preparation",
                "options": [
                    "CBSE/State Board: Physics, Chemistry, Biology (PCB)",
                    "Dedicated NEET coaching (Allen, Aakash, BYJU's etc.)",
                    "Minimum 50% in PCB for NEET eligibility",
                ],
                "duration": "2 years",
                "notes": "NEET is the single gateway for all MBBS admissions in India. Target 600+ for government medical colleges."
            },
            {
                "level": "undergraduate",
                "title": "MBBS (Bachelor of Medicine, Bachelor of Surgery)",
                "options": [
                    "Government Medical Colleges (via NEET) — AIIMs, JIPMER, GMCs",
                    "Private Medical Colleges (high fees: ₹50L–₹1Cr+)",
                    "Duration: 5.5 years including 1 year internship",
                ],
                "duration": "5.5 years",
                "notes": "Internship is mandatory. MCI registration after completion."
            },
            {
                "level": "postgraduate",
                "title": "MD/MS Specialization (Optional but recommended)",
                "options": [
                    "NEET PG for MD/MS admission",
                    "Specializations: General Medicine, Surgery, Pediatrics, Psychiatry, Radiology, etc.",
                    "Super-specialization (DM/MCh) after MD/MS",
                ],
                "duration": "3 years",
                "notes": "Specialists earn significantly more. Government service (bond) may be required after some govt colleges."
            }
        ]
    },

    "path_ca": {
        "target_professions": ["BIZ001"],
        "stages": [
            {
                "level": "high_school",
                "title": "9th–10th: Build strong Maths foundation",
                "options": [
                    "Commerce stream preferred (can also do from Science)",
                    "Strong Maths and English skills essential",
                ],
                "duration": "2 years",
                "notes": "CA Foundation can be attempted after 10th board exams."
            },
            {
                "level": "higher_sec",
                "title": "11th–12th: Commerce + Register for CA Foundation",
                "options": [
                    "Commerce with Accounts, Economics, Business Studies, Maths",
                    "Register for ICAI CA Foundation Course",
                    "Appear for CA Foundation exam after 12th",
                ],
                "duration": "2 years",
                "notes": "CA Foundation has 4 papers. Pass all to move to CA Intermediate."
            },
            {
                "level": "undergraduate",
                "title": "CA Intermediate + Articleship",
                "options": [
                    "CA Intermediate: 8 papers (can pursue B.Com simultaneously)",
                    "3-year Articleship with a CA firm — mandatory practical training",
                    "B.Com (Hons) at Delhi University or equivalent for academic backup",
                ],
                "duration": "3–4 years",
                "notes": "Articleship gives real-world exposure to audit, tax, accounts. Very demanding period."
            },
            {
                "level": "postgraduate",
                "title": "CA Final — Become a Chartered Accountant",
                "options": [
                    "CA Final: 8 papers (hardest stage — 10–15% pass rate)",
                    "After passing: membership of ICAI, use of 'CA' designation",
                    "Optional: CPA (USA), ACCA (UK) for global practice",
                ],
                "duration": "1–2 years",
                "notes": "Average time to complete CA: 4.5–6 years from Foundation. Extremely respected and well-paying in India."
            }
        ]
    },

    "path_civil_services": {
        "target_professions": ["LAW002"],
        "stages": [
            {
                "level": "higher_sec",
                "title": "11th–12th: Any stream — focus on GK & reading",
                "options": [
                    "Humanities/Arts preferred for background knowledge",
                    "Science also fine — many IAS officers come from engineering",
                    "Start reading The Hindu, NCERT books from now",
                ],
                "duration": "2 years",
                "notes": "Stream doesn't matter for UPSC. What matters is breadth of knowledge."
            },
            {
                "level": "undergraduate",
                "title": "Any Bachelor's Degree + UPSC Preparation",
                "options": [
                    "B.A. History/Political Science/Sociology — natural fit",
                    "B.A./B.Sc./B.Tech/LLB/MBBS — all eligible",
                    "Colleges: Delhi University, JNU, BHU preferred for environment",
                    "Start UPSC prep from 2nd year onwards",
                    "Optional: Join coaching (Chanakya IAS, Vision IAS, etc.)",
                ],
                "duration": "3–4 years",
                "notes": "UPSC can be attempted from age 21. 6 attempts for General, 9 for OBC, unlimited for SC/ST."
            },
            {
                "level": "working",
                "title": "UPSC Civil Services Examination",
                "options": [
                    "Prelims → Mains → Personality Test (Interview)",
                    "Optional subject selection for Mains is strategic",
                    "Expected preparation time: 1–3 years dedicated study",
                ],
                "duration": "1–3 years",
                "notes": "One of the most competitive exams in the world. ~1M appear, ~1000 selected."
            }
        ]
    },

    "path_data_scientist": {
        "target_professions": ["TECH002", "TECH005"],
        "stages": [
            {
                "level": "higher_sec",
                "title": "11th–12th: Science with Maths — mandatory",
                "options": [
                    "PCM (Physics, Chemistry, Maths) — preferred",
                    "Computer Science as additional subject — advantage",
                ],
                "duration": "2 years",
                "notes": "Statistics and Maths are the foundation of Data Science."
            },
            {
                "level": "undergraduate",
                "title": "B.Tech CS / B.Sc Statistics / B.Sc Maths / B.Sc Data Science",
                "options": [
                    "B.Tech CS/IT at IIT/NIT/BITS — strongest pathway",
                    "B.Sc Statistics at IISc, CMI, ISI Kolkata",
                    "B.Sc Mathematics at IISc, IITs",
                    "B.Sc Data Science at newer universities",
                    "Learn Python, R, SQL, ML independently",
                ],
                "duration": "3–4 years",
                "notes": "Build a GitHub portfolio. Kaggle competitions crucial for entry-level jobs."
            },
            {
                "level": "postgraduate",
                "title": "M.Tech / M.Sc / MS in Data Science / Statistics / AI",
                "options": [
                    "M.Tech Data Science at IITs (via GATE)",
                    "M.Sc Statistics at ISI Delhi/Kolkata",
                    "MS/PhD in USA/Canada for research roles",
                    "PG Diploma: IIIT Bangalore, Great Learning, Upgrad",
                ],
                "duration": "2 years",
                "notes": "Not mandatory — many data scientists enter industry after B.Tech with strong portfolio."
            }
        ]
    },
}