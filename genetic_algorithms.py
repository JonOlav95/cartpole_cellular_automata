import random
from individual import Individual
import numpy.random as npr
from mutation import mutate, ca_mutate


# Creates an initial population with random genes
def initial_population():
    individuals = []

    for j in range(100):

        # Choose the length of the chromosome at random
        sequence_size = random.randint(2, 5)

        individual = Individual(length=sequence_size)

        for i in range(sequence_size):
            # Choose the genes in the chromosome at random
            gene = random.randint(0, 255)
            individual.chromosome.append(gene)

        individual.chromosome_ca = generate_ca_cut()
        individuals.append(individual)

    return individuals


# Creates a random individual
def generate_individual():
    size = random.randint(2, 5)
    individual = Individual(length=size)

    for i in range(size):
        gene = random.randint(0, 255)
        individual.chromosome.append(gene)

    individual.chromosome_ca = generate_ca_cut()

    return individual


# Creates random cut ranges for the observation ranges
def generate_ca_cut():
    ca_cut = [0.0] * 4
    ca_cut[0] = random.randint(1, 800) / 1000
    ca_cut[1] = random.randint(1, 2000) / 1000
    ca_cut[2] = random.randint(1, 240) / 1000
    ca_cut[3] = random.randint(1, 1000) / 2000

    return ca_cut


# Uniform crossover on the ca chromosome
def uniform_crossover_ca(ca_1, ca_2):

    child_1 = [0] * 4
    child_2 = [0] * 4

    for i in range(4):
        flip = random.randint(0, 1)

        if flip == 1:
            child_1[i] = ca_1[i]
            child_2[i] = ca_2[i]
        else:
            child_1[i] = ca_2[i]
            child_2[i] = ca_1[i]

    return child_1, child_2


def random_offspring(parent_1, parent_2):

    if len(parent_1.chromosome) != len(parent_2.chromosome):
        return False

    for gene in parent_1.chromosome:
        if gene not in parent_2.chromosome:
            return False

    if parent_1.reward == 500 and parent_2.reward == 500:
        return False

    return True


def uniform_crossover_flip(p_c, c1_len, c2_len, c1_c, c2_c):
    for gene in p_c:
        if len(c1_c) >= c1_len:
            c2_c.append(gene)
            continue

        if len(c2_c) >= c2_len:
            c1_c.append(gene)
            continue

        flip = random.randint(0, 1)
        if flip == 0:
            c1_c.append(gene)

        elif flip == 1:
            c2_c.append(gene)


def uniform_crossover(p1, p2):

    if random_offspring(p1, p2):
        print("Creating random offspring")
        individual_1 = generate_individual()
        individual_2 = generate_individual()

        return individual_1, individual_2

    c1_ca = p1.chromosome_ca
    c2_ca = p2.chromosome_ca

    p1_c = p1.chromosome
    p2_c = p2.chromosome

    c1_c = []
    c2_c = []

    c1_len = len(p1_c)
    c2_len = len(p2_c)

    uniform_crossover_flip(p1_c, c1_len, c2_len, c1_c, c2_c)
    uniform_crossover_flip(p2_c, c1_len, c2_len, c1_c, c2_c)

    individual_1 = Individual(len(c1_c))
    individual_2 = Individual(len(c2_c))

    individual_1.chromosome = c1_c
    individual_2.chromosome = c2_c

    individual_1.chromosome_ca = c1_ca
    individual_2.chromosome_ca = c2_ca

    return individual_1, individual_2



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
    total_remove = 94

    # Elitism
    new_population = population[:(len(population) - total_remove)]

    max_reward = sum([c.reward for c in population])
    selection_probs = [c.reward / max_reward for c in population]

    for i in range(int(total_remove / 2)):
        parent_1 = None
        parent_2 = None

        while parent_1 == parent_2:
            parent_1 = population[npr.choice(len(population), p=selection_probs)]
            parent_2 = population[npr.choice(len(population), p=selection_probs)]

        c1, c2 = uniform_crossover(parent_1, parent_2)
        ca_1, ca_2 = uniform_crossover_ca(c1.chromosome_ca, c2.chromosome_ca)

        c1.chromosome = mutate(c1.chromosome)
        c2.chromosome = mutate(c2.chromosome)

        ca_1 = ca_mutate(ca_1)
        ca_2 = ca_mutate(ca_2)

        c1.chromosome_ca = ca_1
        c2.chromosome_ca = ca_2

        new_population.append(c1)
        new_population.append(c2)

    return new_population
