from google.adk.agents import Agent
from utils.skill_extractor import extract_skills

MODEL = "gemini-2.0-flash"

def get_resume_skills(resume_text: str) -> dict:
    """Extract skills from resume text using the local skills taxonomy."""
    return {"skills": extract_skills(resume_text)}

root_agent = Agent(
    name="resume_analysis_agent",
    model=MODEL,
    description="Analyzes resume content and extracts candidate evidence and skills.",
    instruction=(
        "You are a resume analysis specialist. Summarize education, experience, projects, "
        "tools and achievements from the supplied resume. Separate explicit evidence from "
        "inference. Never invent qualifications or metrics. Identify strengths relevant "
        "to the user's target role and mention missing information."
    ),
    tools=[get_resume_skills],
)
