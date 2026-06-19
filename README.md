# AI Career Assistant using Google ADK

This beginner-friendly Python project shows a simple multi-agent career assistant using a Google Agent Development Kit style structure.

The app uses four small agents:

- Resume Agent: extracts skills, education, projects, and experience from resume text.
- Job Matching Agent: compares the resume with a job description.
- Skill Gap Agent: finds missing skills from the job description.
- Coordinator Agent: combines everything into a final recommendation.

The code is intentionally simple so you can understand how the agents work together before adding a real LLM.

`main.py` also defines a Google ADK `root_agent` that can call the career analysis tool when `google-adk` is installed.

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── .env.example
├── agent.py
├── main.py
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

## Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
```

On Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create your environment file.

```bash
copy .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

4. Add your Google API key to `.env` if you want to connect this project to Google ADK or Gemini later.

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

## Notes

- This project includes the `google-adk` dependency in `requirements.txt`.
- The command `python main.py` uses simple Python logic so it can run without an API key.
- The command `adk run .` uses Google ADK after dependencies and credentials are configured.
- You can later replace the rule-based logic inside each specialist agent with deeper LLM prompts.
