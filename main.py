import gym
from ca_functions import *
from genetic_algorithms import *
from individual import *

""" Sequence of the program:
    
An initial population of 100 is created
Each potential solution in the population runs in the simulation
A new population is created by the best performers in the previous population

"""


# Generate the initial population before the simulation begins
def initial_population():
    chromosomes = []

    for j in range(100):

        # Choose the length of the chromosome at random
        sequence_size = random.randint(1, 5)

        chromosome = Individual(length=sequence_size)

        for i in range(sequence_size):
            # Choose the genes in the chromosome at random
            gene = random.randint(0, 255)
            chromosome.append_gene(gene)

        chromosomes.append(chromosome)

    return chromosomes


if __name__ == '__main__':

    env = gym.make("CartPole-v1")
    observation = env.reset()

    population = initial_population()

    # Run the simulation for 1000 generations (steps)
    for generation in range(1000):

        # Used to calculate the total reward of each generation
        total_reward = 0

        # Run each solution in the population until it is done
        for solution in population:

            # Used to calculate the individual reward of each potential solution
            solution_reward = 0

            while True:

                # Activate rendering after 500 generations
                if generation > 500:
                    env.render()

                # Create a cellular automata array from the observation
                ca_arr = ca_generate(observation)

                # Apply the solutions rules to the cellular automata and return an action
                action = rules_to_action(ca_arr, solution)

                observation, reward, done, info = env.step(action)
                solution_reward += reward

                if done:
                    observation = env.reset()
                    break

            solution.set_reward(solution_reward)
            total_reward += solution_reward

        # Generate a new population by using genetic algorithms
        population = generate(population)

        print("sum rewards: ", str(total_reward))
        print("tot: ", str(len(population)))

    env.close()
