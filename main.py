import gym
from genetic_algorithms import *
from simulation import simulate
import csv

""" Sequence of the program:
    
An initial population of 100 is created
Each potential solution in the population runs in the simulation
A new population is created by the best performers in the previous population

"""


def store_data(pop, gen, rew):
    pop = sorted(pop, key=lambda x: x.reward, reverse=True)

    filename = "data/" + str(gen) + "_" + str(rew) + ".txt"

    with open(filename, mode="w") as file:
        file.write("Generation: " + str(gen) + "\tTotal Reward: " + str(rew) + "\n")

        for s in pop:
            file.write("Reward: " + str(s.reward) + "   \tchromosome: " + str(s.get_chromosome()) + "\n")


if __name__ == '__main__':

    env = gym.make("CartPole-v1")
    population = initial_population()

    # Run the simulation for 1000 generations (steps)
    for generation in range(1000):

        # Used to calculate the total reward of each generation
        total_reward = 0

        # Run each solution in the population until it is done
        for solution in population:
            reward = simulate(env, solution)
            total_reward += reward

        # Generate a new population by using genetic algorithms
        store_data(population, generation, total_reward)
        population = generate(population)

        print("generation: ", str(generation))
        print("sum rewards: ", str(total_reward))

    env.close()
