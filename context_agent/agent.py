from google.adk.agents.llm_agent import Agent
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M")

def get_location():
    return "South India"

root_agent = Agent(
    model='gemini-2.5-flash',
    name="ContextAgent",
    description='A helpful assistant for user food related questions.',
    instruction="""
    Use available tools to determine:
    - current time
    - user location
    Output JSON only.
    """,
    tools=[get_current_time, get_location]
)