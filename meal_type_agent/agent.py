from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='MealAgent',
    description='A helpful assistant for user questions.',
    instruction="""
    Determine meal type based on time:
    6–10 breakfast
    12–15 lunch
    18–22 dinner
    otherwise snack

    Output JSON only.
    """,
)
