from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

from preference_agent.agent import root_agent as preference_agent
from context_agent.agent import root_agent as context_agent
from meal_type_agent.agent import root_agent as meal_agent
from cuisine_mapping_agent.agent import root_agent as cuisine_agent
from dish_selection_agent.agent import root_agent as dish_agent
from recipe_generation_agent.agent import root_agent as recipe_agent


root_agent = Agent(
    model='gemini-2.5-flash',
    name='OrchestratorAgent',
    description='A helpful assistant for user food questions.',
    instruction="""
    You are a controller agent.
    Every subagent is a agent as a tool you can call.
    Steps:
    1. Ask preference_agent to classify user input
    2. Without any context ask context_agent for time and location
    3. With preference and time and place context from context_agent ask meal_agent to determine meal type
    4. Then ask cuisine_agent to map cuisines
    5. Then ask dish_agent to choose dish
    6. Then ask recipe_agent to generate recipe
    Every subagent is a agent as a tool you can call.
    Produce final recipe as output.
    """,
    tools=[
        AgentTool(preference_agent),
        AgentTool(context_agent),
        AgentTool(meal_agent),
        AgentTool(cuisine_agent),
        AgentTool(dish_agent),
        AgentTool(recipe_agent)
    ]
)