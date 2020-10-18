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


def uniform_binary_tmp(p1_binary, p2_binary):

    c1 = []
    c2 = []
    for i in range(len(p2_binary)):

        gene_1 = []
        gene_2 = []
        for j in range(8):
            flip = random.randint(0, 1)

            if flip == 1:
                gene_1.append(p1_binary[i][j])
                gene_2.append(p2_binary[i][j])
            else:
                gene_1.append(p2_binary[i][j])
                gene_2.append(p1_binary[i][j])

        c2.append(gene_1)
        c1.append(gene_2)

    for i in range(len(p2_binary), len(p1_binary)):
        gene_1 = []
        for j in range(8):
            gene_1.append(p1_binary[i][j])

        c1.append(gene_1)

    return c1, c2


def uniform_crossover_binary(p1, p2):
    if random_offspring(p1, p2):
        print("Generating random offspring")
        individual_1 = generate_individual()
        individual_2 = generate_individual()

        return individual_1, individual_2

    c1_ca = p1.chromosome_ca
    c2_ca = p2.chromosome_ca

    p1 = p1.chromosome
    p2 = p2.chromosome

    p1_binary = []
    p2_binary = []
    for rule_id in p1:
        p1_binary.append(list(map(int, format(rule_id, "#010b")[2:])))

    for rule_id in p2:
        p2_binary.append(list(map(int, format(rule_id, "#010b")[2:])))

    if len(p1) > len(p2):
        c1, c2 = uniform_binary_tmp(p1_binary, p2_binary)
    else:
        c2, c1 = uniform_binary_tmp(p2_binary, p1_binary)


    for i in range(len(c1)):
        c1[i] = int("".join(str(x) for x in c1[i]), 2)

    for j in range(len(c2)):
        c2[j] = int("".join(str(x) for x in c2[j]), 2)

    individual_1 = Individual(len(c1))
    individual_2 = Individual(len(c2))

    individual_1.chromosome = c1
    individual_2.chromosome = c2

    individual_1.chromosome_ca = c1_ca
    individual_2.chromosome_ca = c2_ca

    return individual_1, individual_2


def uniform_crossover(p1, p2):

    if random_offspring(p1, p2):
        print("Generating random offspring")
        individual_1 = generate_individual()
        individual_2 = generate_individual()

        return individual_1, individual_2

    c1_ca = p1.chromosome_ca
    c2_ca = p2.chromosome_ca

    p1 = p1.chromosome
    p2 = p2.chromosome

    c1 = [0] * len(p1)
    c2 = [0] * len(p2)

    if len(p1) > len(p2):
        longest = len(p1)
        shortest = len(p2)
    else:
        longest = len(p2)
        shortest = len(p1)

    for i in range(shortest):
        flip = random.randint(0, 1)

        if flip == 1:
            c1[i] = p1[i]
            c2[i] = p2[i]
        else:
            c1[i] = p2[i]
            c2[i] = p1[i]

    for i in range(shortest, longest):
        if len(p1) > len(p2):
            c1[i] = p1[i]
        else:
            c2[i] = p2[i]

    individual_1 = Individual(len(c1))
    individual_2 = Individual(len(c2))

    individual_1.chromosome = c1
    individual_2.chromosome = c2

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

        c1, c2 = uniform_crossover_binary(parent_1, parent_2)
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
