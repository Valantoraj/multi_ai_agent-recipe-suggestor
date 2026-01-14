from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='CuisineAgent',
    description='A helpful assistant for user questions.',
    instruction="""
    Map the user's location to relevant local cuisines.

    Example:
    South India → South Indian, Chettinad, Kerala

    Output JSON list only.
    """,
)
