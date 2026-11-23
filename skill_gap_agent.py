from google.adk.agents import Agent
from utils.skill_extractor import extract_skills, identify_skill_gaps

MODEL = "gemini-2.0-flash"

def find_skill_gaps(resume_text: str, job_description: str) -> dict:
    """Find job-description skills not explicitly detected in the resume."""
    return identify_skill_gaps(extract_skills(resume_text), extract_skills(job_description))

root_agent = Agent(
    name="skill_gap_agent",
    model=MODEL,
    description="Prioritizes skills not demonstrated by the candidate's resume.",
    instruction=(
        "You are a skill-gap analyst. Prioritize missing or weakly evidenced requirements "
        "as must-have, useful or optional. Suggest a practical way to demonstrate each skill. "
        "Use the phrase 'not demonstrated' rather than claiming the candidate cannot do it."
    ),
    tools=[find_skill_gaps],
)
