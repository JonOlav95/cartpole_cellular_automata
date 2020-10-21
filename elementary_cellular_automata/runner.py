import gym
from elementary_cellular_automata.cellular_automata import ca_generate, converge_action
from elementary_cellular_automata.data_handling import store_data
from elementary_cellular_automata.genetic_algorithms import *
from elementary_cellular_automata.helper_funcs import initial_population


def simulate(env, solution):
    """Runs one solution in the environment

    Args:
        env: An OpenAI environment.
        solution: A solution which is a list of the object Individual.

    Returns:
        The reward (fitness) the solution obtained during the simulation.
    """
    solution_reward = 0
    observation = env.reset()

    while True:

        # Create a cellular automata array from the observation
        ca_arr = ca_generate(observation, solution.chromosome_ca)

        # Apply the solutions rules to the cellular automata and return an action
        action = converge_action(ca_arr, solution)

        observation, reward, done, info = env.step(action)
        solution_reward += reward

        if done:
            solution.set_reward(int(solution_reward))
            return solution_reward


def main():
    """Creates the CartPole environment version 1 (maximum 500 reward) and applies the population"""
    env = gym.make("CartPole-v1")
    population = initial_population()

    for generation in range(1000):

        # Used to calculate the total reward of each generation
        total_reward = 0

        # Run each solution in the population until it is done
        for solution in population:
            reward = simulate(env, solution)
            total_reward += reward

        #store_data(population, generation, total_reward)

        # Generate a new population by using genetic algorithms
        population = generate(population)

        print("generation: ", str(generation))
        print("sum rewards: ", str(total_reward))

    env.close()


if __name__ == '__main__':
    main()
