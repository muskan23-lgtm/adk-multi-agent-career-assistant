# AI Career Assistant using Google ADK

A beginner-friendly Python project that shows how to organize a simple multi-agent career assistant with Google Agent Development Kit (ADK).

The project has four agents:

- **Resume Agent**: reads a resume and extracts strengths, experience, and skills.
- **Job Matching Agent**: compares a resume with a job description.
- **Skill Gap Agent**: finds missing skills and suggests learning steps.
- **Coordinator Agent**: combines the work of the other agents into one career report.

The code is intentionally simple and heavily commented so you can understand the project structure before adding more advanced ADK features.

## Project Structure

```text
.
├── main.py
├── requirements.txt
├── .env.example
├── agents/
│   ├── __init__.py
│   ├── resume_agent.py
│   ├── job_match_agent.py
│   ├── skill_gap_agent.py
│   └── coordinator_agent.py
└── data/
    ├── sample_resume.txt
    └── sample_job_description.txt
```

## What This Project Does

When you run the app, it:

1. Loads a sample resume from `data/sample_resume.txt`.
2. Loads a sample job description from `data/sample_job_description.txt`.
3. Uses small Python functions to simulate each agent's role.
4. Creates Google ADK `Agent` objects so you can see how the same agents would be represented in ADK.
5. Prints a simple career analysis report in the terminal.

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

On Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create your environment file

Copy `.env.example` to `.env`:

```bash
copy .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

Then add your Google API key in `.env`.

## Run

```bash
python main.py
```

You should see a career assistant report printed in the terminal.

## Notes for Beginners

- The project uses regular Python functions for the first working version.
- The ADK `Agent` objects are created in the `agents/` files.
- This makes the project easy to run locally while still teaching the multi-agent structure.
- Later, you can connect the agents to live Gemini responses using Google ADK runners and sessions.

## Next Ideas

- Accept a resume file path from the command line.
- Save the report as Markdown.
- Add an interview preparation agent.
- Add a cover letter generation agent.
- Build a small Streamlit or FastAPI interface.
