from preference_agent.agent import root_agent as preference_agent
from context_agent.agent import root_agent as context_agent
from meal_type_agent.agent import root_agent as meal_agent
from cuisine_mapping_agent.agent import root_agent as cuisine_agent
from dish_selection_agent.agent import root_agent as dish_agent
from recipe_generation_agent.agent import root_agent as recipe_agent

def run_food_agent_system(user_input):
    state = {}

    state["preferences"] = preference_agent(user_input)
    state["context"] = context_agent()
    state["meal_type"] = meal_agent(state["context"])
    state["cuisines"] = cuisine_agent(state["context"])
    state["dish"] = dish_agent(state)
    state["recipe"] = recipe_agent(state["dish"])
    return state["recipe"]
