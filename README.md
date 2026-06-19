# AI Career Assistant using Google ADK

A beginner-friendly Python project that shows how to organize a simple multi-agent career assistant with Google Agent Development Kit (ADK).

The app uses four small agents:

- Resume Agent: extracts skills, education, projects, and experience from resume text.
- Job Matching Agent: compares the resume with a job description.
- Skill Gap Agent: identifies missing skills and suggests learning steps.
- Coordinator Agent: combines all agent outputs into one final recommendation.

The code is intentionally simple and heavily commented so you can understand the project structure before adding more advanced ADK features.

`main.py` also defines a Google ADK `root_agent` that can call the career analysis tool when `google-adk` is installed. The `agent.py` file exposes that `root_agent` for ADK.

## Project Structure

```text
.
|-- README.md
|-- requirements.txt
|-- .env.example
|-- agent.py
|-- main.py
|-- agents/
|   |-- __init__.py
|   |-- resume_agent.py
|   |-- job_match_agent.py
|   |-- skill_gap_agent.py
|   `-- coordinator_agent.py
`-- data/
    |-- sample_resume.txt
    `-- sample_job_description.txt
```

## What This Project Does

When you run the app, it:

1. Loads a sample resume from `data/sample_resume.txt`.
2. Loads a sample job description from `data/sample_job_description.txt`.
3. Runs the Resume Agent, Job Matching Agent, and Skill Gap Agent.
4. Uses the Coordinator Agent to combine all results.
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

Then add your Google API key in `.env` if you want to run the ADK agent with Google services.

## Run the Beginner Python Demo

```bash
python main.py
```

The program reads the sample resume and sample job description from the `data/` folder, runs each agent, and prints a final career recommendation.

## Run with Google ADK

After installing dependencies and setting `GOOGLE_API_KEY` in `.env`, you can experiment with the ADK agent.

```bash
adk run .
```

The ADK `root_agent` is created in `main.py` and exposed through `agent.py`. It uses the `analyze_career_fit` tool function to call the coordinator agent.

## Notes for Beginners

- The command `python main.py` uses simple Python logic so it can run without an API key.
- The command `adk run .` uses Google ADK after dependencies and credentials are configured.
- You can later replace the rule-based logic inside each specialist agent with deeper LLM prompts.

## Next Ideas

- Accept a resume file path from the command line.
- Save the report as Markdown.
- Add an interview preparation agent.
- Add a cover letter generation agent.
- Build a small Streamlit or FastAPI interface.
