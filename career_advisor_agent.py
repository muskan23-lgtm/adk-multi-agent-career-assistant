from google.adk.agents import Agent

MODEL = "gemini-2.0-flash"

root_agent = Agent(
    name="career_advisor_agent",
    model=MODEL,
    description="Creates role recommendations and realistic learning roadmaps.",
    instruction=(
        "You are a practical early-career advisor. Based only on the profile and target role "
        "provided, recommend suitable adjacent roles, portfolio projects, interview topics "
        "and a realistic 30-day learning plan. Do not guarantee selection or invent experience."
    ),
)
