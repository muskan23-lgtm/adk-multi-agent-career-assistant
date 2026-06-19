"""Run the AI Career Assistant multi-agent demo."""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    # The app can still run before dependencies are installed.
    def load_dotenv() -> None:
        """Use a no-op fallback when python-dotenv is not installed yet."""
        return None

try:
    from google.adk.agents.llm_agent import Agent
except ImportError:
    # The rule-based demo still works before google-adk is installed.
    Agent = None

from agents.coordinator_agent import CoordinatorAgent


# Store paths in constants so they are easy to change later.
PROJECT_ROOT = Path(__file__).parent
RESUME_PATH = PROJECT_ROOT / "data" / "sample_resume.txt"
JOB_DESCRIPTION_PATH = PROJECT_ROOT / "data" / "sample_job_description.txt"


def analyze_career_fit(resume_text: str, job_description_text: str) -> dict:
    """ADK tool function that returns a career fit report."""
    coordinator = CoordinatorAgent()
    report = coordinator.create_recommendation(
        resume_text=resume_text,
        job_description_text=job_description_text,
    )

    return {
        "status": "success",
        "report": report,
    }


def create_root_agent() -> object | None:
    """Create the Google ADK root agent when google-adk is installed."""
    if Agent is None:
        return None

    # The model name can be changed in the .env file.
    model_name = os.getenv("GOOGLE_MODEL", "gemini-flash-latest")

    return Agent(
        model=model_name,
        name="career_coordinator_agent",
        description="Coordinates resume analysis and job matching.",
        instruction=(
            "You are an AI Career Assistant. Ask the user for resume text and a "
            "job description, then call analyze_career_fit to create a final "
            "recommendation."
        ),
        tools=[analyze_career_fit],
    )


def read_text_file(file_path: Path) -> str:
    """Read text from a file and return it as a string."""
    return file_path.read_text(encoding="utf-8")


def main() -> None:
    """Load sample data, run the coordinator, and print the final report."""
    # Load environment variables from .env if the file exists.
    load_dotenv()

    # Read the sample resume and job description.
    resume_text = read_text_file(RESUME_PATH)
    job_description_text = read_text_file(JOB_DESCRIPTION_PATH)

    # The coordinator calls all other agents and combines their outputs.
    coordinator = CoordinatorAgent()
    final_report = coordinator.create_recommendation(
        resume_text=resume_text,
        job_description_text=job_description_text,
    )

    # Print the final result in the terminal.
    print(final_report)


if __name__ == "__main__":
    main()


# Google ADK looks for a root_agent object when running an agent project.
load_dotenv()
root_agent = create_root_agent()
