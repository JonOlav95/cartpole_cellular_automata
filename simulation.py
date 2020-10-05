from ca_functions import ca_generate, generate_action


# Runs the simulation once given a solution used to calculate the actions
def simulate(env, solution):

    solution_reward = 0
    observation = env.reset()

    while True:

        # Create a cellular automata array from the observation
        ca_arr = ca_generate(observation)

        # Apply the solutions rules to the cellular automata and return an action
        action = generate_action(ca_arr, solution)

        observation, reward, done, info = env.step(action)
        solution_reward += reward

        if done:
            solution.set_reward(int(solution_reward))
            return solution_reward
