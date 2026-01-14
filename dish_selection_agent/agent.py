from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='DishSelectorAgent',
    description='A helpful assistant for user food related questions.',
    instruction="""
    Select ONE suitable dish based on:
    - food preferences
    - meal type
    - local cuisines

    Prefer regional dishes.
    Output dish name only.
    """,
)
