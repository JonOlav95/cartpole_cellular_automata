import random

from genetic_algorithms import generate_individual, generate_ca_cut
from individual import Individual





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

    '''
    if random_offspring(p1, p2):
        print("Creating random offspring")
        individual_1 = generate_individual()
        individual_2 = generate_individual()

        return individual_1, individual_2
    '''

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
