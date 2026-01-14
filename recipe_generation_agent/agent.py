from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='RecipeAgent',
    description='A helpful assistant for user food related questions.',
    instruction="""
    Generate a simple home-style recipe.
    Include:
    - ingredients list
    - step-by-step preparation

    Keep it concise and easy.
    """,
)
