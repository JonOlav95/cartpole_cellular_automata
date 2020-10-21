import numpy.random as npr
import random
from artifical_neural_network.individual import Individual


def mutate(chromosome):
    """Mutates the chromosome by randomly changing zero or more values.

    Args:
        chromosome: The list of numbers that will be mutated.

    Returns:
        A list of the same size which may or may not be mutated.
    """
    while True:
        chance = random.randint(0, 1)
        if chance != 0:
            return chromosome

        index = random.randint(0, len(chromosome) - 1)
        weight = random.uniform(-1, 1)
        chromosome[index] = weight

        return chromosome


def uniform_crossover(p1_chromosome, p2_chromosome):
    """Uniform crossover between two parents to produce two offspring.

    Takes all the values from the parents and randomly split them
    between the offsprings.

    Args:
        p1_chromosome: The first parent, a list of numbers.
        p2_chromosome: The second parent, A list of numbers.
    Returns:
        Two lists of numbers which represent the offspring of
        the two parents.
    """
    c1_chromosome = []
    c2_chromosome = []

    for i in range(len(p1_chromosome)):
        flip = random.randint(0, 1)

        if flip == 1:
            c1_chromosome.append(p1_chromosome[i])
            c2_chromosome.append(p2_chromosome[i])
        else:
            c1_chromosome.append(p2_chromosome[i])
            c2_chromosome.append(p1_chromosome[i])

    return c1_chromosome, c2_chromosome


def wheel_selection(total_offspring, population):
    """Wheel selection used to select parents.

    High reward parents have a higher chance of being chosen.

    Args:
        total_offspring: The total amount of offspring the new population requires.
        population: The population of potential parents.
    """
    max_reward = sum([c.reward for c in population])
    selection_prob = [c.reward / max_reward for c in population]

    parents_1 = []
    parents_2 = []

    for i in range(int(total_offspring / 2)):

        p1 = None
        p2 = None

        while p1 == p2:
            p1 = population[npr.choice(len(population), p=selection_prob)]
            p2 = population[npr.choice(len(population), p=selection_prob)]

        parents_1.append(p1)
        parents_2.append(p2)

    return parents_1, parents_2


def survival(population):
    """Applies the evolutionary survival process to the population

    A few select elites with the best reward (fitness) is automatically part of the next generation.
    From the population parents are selected to create offspring. The offspring will be part of
    the next generation. The parents will cease to exist unless they were part of the elite.
    Mutation is applied to the offspring, which has a chance of altering the chromosomes.

    Args:
        The population which is a list of the object Individual. The entire population just ran in
        the simulation and their reward (fitness) was stored.

    Returns:
        A new population which is a list of the object Individual. The new population is the next generation
        and consists of the elite from the previous population and offspring from the previous generation.
    """

    # Sort the population by its reward (fitness)
    population = sorted(population, key=lambda x: x.reward, reverse=True)
    total_remove = 94

    # Elitism
    new_population = population[:(len(population) - total_remove)]

    parent_1, parent_2 = wheel_selection(total_remove, population)

    for i in range(int(total_remove / 2)):
        weight_1, weight_2 = uniform_crossover(parent_1[i].chromosome, parent_2[i].chromosome)
        bias_1, bias_2 = uniform_crossover(parent_1[i].bias_chromosome, parent_2[i].bias_chromosome)

        mutate(weight_1)
        mutate(weight_2)
        mutate(bias_1)
        mutate(bias_2)

        c1 = Individual()
        c2 = Individual()

        c1.chromosome = weight_1
        c1.bias_chromosome = bias_1

        c2.chromosome = weight_2
        c2.bias_chromosome = bias_2

        new_population.append(c1)
        new_population.append(c2)

    return new_population
