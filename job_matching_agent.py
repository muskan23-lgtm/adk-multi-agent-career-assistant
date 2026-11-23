from google.adk.agents import Agent
from utils.ats_scorer import score_resume_job

MODEL = "gemini-2.0-flash"

def calculate_job_match(resume_text: str, job_description: str) -> dict:
    """Calculate transparent baseline overlap between resume and job description."""
    return score_resume_job(resume_text, job_description)

root_agent = Agent(
    name="job_matching_agent",
    model=MODEL,
    description="Compares resume evidence with job requirements and explains fit.",
    instruction=(
        "You are a job-matching specialist. Compare the resume with the job description. "
        "Explain strong matches, partial matches and requirements not demonstrated. "
        "Do not treat absent keywords as proof that the candidate lacks a skill. "
        "Any numerical score must be described as an estimate, never an official ATS score."
    ),
    tools=[calculate_job_match],
)
