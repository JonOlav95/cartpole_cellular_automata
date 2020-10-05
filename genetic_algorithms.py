import copy
import random
from random import choice
from individual import Individual


# Generate the initial population before the simulation begins
from mutation import mutate


def initial_population():
    chromosomes = []

    for j in range(100):

        # Choose the length of the chromosome at random
        sequence_size = random.randint(2, 5)

        chromosome = Individual(length=sequence_size)

        for i in range(sequence_size):
            # Choose the genes in the chromosome at random
            gene = random.randint(0, 255)
            chromosome.append_gene(gene)

        chromosomes.append(chromosome)

    return chromosomes


def one_point_crossover(parent_1, parent_2):
    maximum_length = len(parent_1) + len(parent_2)

    if maximum_length > 5:
        maximum_length = 5

    child_length = int((len(parent_1) + len(parent_2)) / 2)

    if maximum_length % 2 != 0:
        child_length += random.randint(0, 1)

    cross_point = 0

    if len(parent_1) < len(parent_2):
        lowest_parent = parent_1
        highest_parent = parent_2
        lowest = len(parent_1)
    else:
        lowest_parent = parent_2
        highest_parent = parent_1
        lowest = len(parent_2)

    child = []

    if lowest <= child_length:
        cross_point = random.randint(1, lowest)
        for i in range(cross_point):
            child.append(lowest_parent[i])

        for j in range(cross_point, child_length):
            child.append(highest_parent[j - cross_point])
    else:
        cross_point = random.randint(1, lowest - 1)

    return child


def one_point_crossover_2(parent_1, parent_2):
    child = []
    child_len = int(len(parent_1) + len(parent_2))

    if child_len % 2 == 0:
        child_len = int(child_len / 2)
    else:
        child_len = int(child_len / 2 + random.randint(0, 1))

    if len(parent_1) == 1:
        if len(parent_2) == 1:
            cross_point = random.randint(0, 1)
        else:
            cross_point = 1
    elif child_len > len(parent_1):
        cross_point = random.randint(1, len(parent_1))
    else:
        cross_point = random.randint(1, child_len)

    for i in range(cross_point):
        child.append(parent_1[i])

    curr_len = len(child)

    for i in range(curr_len, child_len):
        if child_len - curr_len > len(parent_2):
            child.append(parent_1[i])

    for j in range(len(child), child_len):
        child.append(parent_2[j - curr_len])

    return child


def generate(population):
    """Generate a new population from the existing population.


    The part of the population that performed best will be
    part of the next population (elitism).

    The part of the population that performed worst will be removed (die).

    The part of the population part of the population that was not removed
    will be used to reproduce children.

    The new population will consist of the elite that survived and the
    children.
    """

    # Sort the population to find out which had the best performance
    population = sorted(population, key=lambda x: x.reward, reverse=True)
    total_remove = 40

    new_population = population[:70]

    population = population[:(len(population) - total_remove)]

    population_copy = copy.copy(population)

    for i in range(int(len(population_copy) / 2)):
        parent_1 = choice(population_copy)
        population_copy.remove(parent_1)

        parent_2 = choice(population_copy)
        population_copy.remove(parent_2)

        c = one_point_crossover_2(parent_1.get_chromosome(), parent_2.get_chromosome())
        c = mutate(c)

        child = Individual(length=len(c))
        child.set_chromosome(c)

        new_population.append(child)

    return new_population
