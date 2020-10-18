import random

from genetic_algorithms import generate_individual, generate_ca_cut
from individual import Individual


def uniform_crossover_2(parent_1, parent_2):

    if parent_1.chromosome == parent_2.chromosome and parent_1.reward != 500 and parent_2.reward != 500:
        individual_1 = generate_individual()
        individual_2 = generate_individual()

        return individual_1, individual_2

    child_1_ca = parent_1.chromosome_ca
    child_2_ca = parent_2.chromosome_ca

    parent_1 = parent_1.chromosome
    parent_2 = parent_2.chromosome

    child_1 = [0] * len(parent_1)
    child_2 = [0] * len(parent_2)

    if len(parent_1) > len(parent_2):
        longest = len(parent_1)
        shortest = len(parent_2)
    else:
        longest = len(parent_2)
        shortest = len(parent_1)

    for i in range(shortest):
        flip = random.randint(0, 1)

        if flip == 1:
            child_1[i] = parent_1[i]
            child_2[i] = parent_2[i]
        else:
            child_1[i] = parent_2[i]
            child_2[i] = parent_1[i]

    for i in range(shortest, longest):
        if len(parent_1) > len(parent_2):
            child_1[i] = parent_1[i]
        else:
            child_2[i] = parent_2[i]

    individual_1 = Individual(len(child_1))
    individual_2 = Individual(len(child_2))

    individual_1.chromosome = child_1
    individual_2.chromosome = child_2

    individual_1.chromosome_ca = child_1_ca
    individual_2.chromosome_ca = child_2_ca

    return individual_1, individual_2



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

