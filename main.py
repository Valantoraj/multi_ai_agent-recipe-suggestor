from coordinating_agent.flow import run_food_agent_system

if __name__ == "__main__":
    #user_input = input("What would you like to eat today? ")
    user_input = "I want a light, spicy meal that's vegan."
    recipe = run_food_agent_system(user_input)
    print(recipe)
