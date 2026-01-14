from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='TouristGuideagent',
    description='A helpful assistant for user to guide users for tourist information.',
    instruction="""
    give response in the below format
    Location: <location_name>
    Description: <short_description>
    Best Time to Visit: <best_time>
    Popular Attractions: <attraction1, attraction2, ...>
    Popular Local Cuisines: <cuisine1, cuisine2, ...>
    """,
)
