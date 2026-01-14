from google.adk.agents.llm_agent import Agent

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

    Steps:
    1. Ask PreferenceAgent to classify user input
    2. Ask ContextAgent for time and location
    3. Ask MealAgent to determine meal type
    4. Ask CuisineAgent to map cuisines
    5. Ask DishSelectorAgent to choose dish
    6. Ask RecipeAgent to generate recipe

    Produce final recipe as output.
    """,
    sub_agents=[
        preference_agent,
        context_agent,
        meal_agent,
        cuisine_agent,
        dish_agent,
        recipe_agent
    ]
)