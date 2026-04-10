"""
Defines which tests are mandatory vs optional for each education level.
Used by the onboarding wizard to build the test schedule.
"""

TEST_SCHEDULE = {

    "middle_school": {
        "mandatory": [
            "logical-reasoning",
            "verbal-ability",
            "interest-ranking",
            "big-five-personality",
        ],
        "optional": [
            "riasec-holland",
            "free-text-profile",
        ],
        "time_limit_override": {
            "logical-reasoning": 45,  # Extra time for younger students (seconds/question)
            "verbal-ability": 35,
        }
    },

    "high_school": {
        "mandatory": [
            "logical-reasoning",
            "verbal-ability",
            "numerical-aptitude",
            "big-five-personality",
            "interest-ranking",
        ],
        "optional": [
            "riasec-holland",
            "free-text-profile",
            "emotional-intelligence",
        ],
        "time_limit_override": {}
    },

    "higher_sec": {
        "mandatory": [
            "logical-reasoning",
            "verbal-ability",
            "numerical-aptitude",
            "big-five-personality",
            "riasec-holland",
            "interest-ranking",
            "values-ranking",
        ],
        "optional": [
            "emotional-intelligence",
            "free-text-profile",
            "spatial-reasoning",
        ],
        "time_limit_override": {}
    },

    "undergraduate": {
        "mandatory": [
            "logical-reasoning",
            "verbal-ability",
            "numerical-aptitude",
            "big-five-personality",
            "riasec-holland",
            "interest-ranking",
            "values-ranking",
            "emotional-intelligence",
        ],
        "optional": [
            "free-text-profile",
            "spatial-reasoning",
            "creativity-index",
        ],
        "time_limit_override": {}
    },

    "postgraduate": {
        "mandatory": [
            "logical-reasoning",
            "verbal-ability",
            "numerical-aptitude",
            "big-five-personality",
            "riasec-holland",
            "values-ranking",
            "emotional-intelligence",
        ],
        "optional": [
            "free-text-profile",
            "creativity-index",
            "leadership-potential",
        ],
        "time_limit_override": {}
    },

    "working": {
        "mandatory": [
            "big-five-personality",
            "riasec-holland",
            "values-ranking",
            "emotional-intelligence",
        ],
        "optional": [
            "logical-reasoning",
            "free-text-profile",
            "leadership-potential",
            "creativity-index",
        ],
        "time_limit_override": {}
    },
}