from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='PreferenceAgent',
    description='A helpful assistant for user food related questions.',
    instruction="""
    Classify food preferences from user text.
    Extract:
    - taste (spicy, sweet, mild)
    - diet (vegan, vegetarian, non-vegetarian)
    - meal heaviness (light, heavy)

    Output JSON only.
    """
)