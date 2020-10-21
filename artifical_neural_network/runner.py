import gym
from artifical_neural_network.genetic_algorithms import survival
from artifical_neural_network.helper_funcs import init_population
from artifical_neural_network.neural_network import init_neural_network


def simulate(env, sol, render):
    """Runs one solution in the environment

    Args:
        env: An OpenAI environment.
        sol: A solution which is a list of the object Individual.
        render: Decides if the simulation should render or not

    Returns:
        The reward (fitness) the solution obtained during the simulation.
    """

    solution_reward = 0
    observation = env.reset()

    neural_network = init_neural_network(sol.chromosome, sol.bias_chromosome)

    while True:

        if render:
            env.render()

        action = neural_network.traverse(observation)

        observation, reward, done, info = env.step(action)
        solution_reward += reward

        if done:
            sol.reward = (int(solution_reward))
            return solution_reward


def main():
    """Creates the CartPole environment version 1 (maximum 500 reward) and applies the population"""

    environment = gym.make("CartPole-v1")
    environment.reset()
    population = init_population()
    render = False

    for generation in range(500000):
        total_reward = 0

        for individual in population:
            total_reward += simulate(environment, individual, render)

        if total_reward > 30000:
            render = True

        print("generation: " + str(generation) + "  reward: " + str(total_reward) + "  length: " + str(len(population)))
        population = survival(population)


if __name__ == '__main__':
    main()

