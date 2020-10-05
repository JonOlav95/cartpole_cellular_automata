import copy
import random
from random import choice
from individual import Individual


def add_gene(child):
    index = random.randint(0, len(child))
    gene = random.randint(0, 255)

    child.insert(index, gene)


def remove_gene(child):
    index = random.randint(0, len(child) - 1)
    child.pop(index)


def modify_gene(child):
    m = random.randint(0, len(child) - 1)
    dc = random.randint(1, 10)
    way = random.randint(0, 1)

    if way == 1:
        if child[m] > 255 - dc:
            child[m] -= dc
        else:
            child[m] += dc
    else:
        if child[m] < dc:
            child[m] += dc
        else:
            child[m] -= dc


def mutate(child):
    mutate_chance = random.randint(0, 4)
    if mutate_chance != 0:
        return child

    if len(child) == 5:
        v_mutation = random.randint(1, 2)

    elif len(child) == 2:
        v_mutation = random.randint(0, 1)

    else:
        v_mutation = random.randint(0, 2)

    if v_mutation == 0:
        add_gene(child)

    elif v_mutation == 1:
        modify_gene(child)

    elif v_mutation == 2:
        remove_gene(child)

    return child


def produce(parent_1, parent_2):
    # 1 to 5
    child_len = int((len(parent_1) + len(parent_2)) / 2)

    if 4 <= child_len < 5:
        child_len += random.randint(0, 1)
    elif 2 <= child_len < 4:
        child_len += random.randint(0, 2)
    elif child_len == 1:
        child_len += random.randint(0, 1)

    child = []
    p1_cpy = copy.copy(parent_1)
    p2_cpy = copy.copy(parent_2)
    total_genes = len(p1_cpy) + len(p2_cpy)

    while total_genes != child_len:

        if len(p1_cpy) == 1:
            c = 0
        elif len(p2_cpy) == 1:
            c = 1
        else:
            c = random.randint(0, 1)

        if c == 0:
            p2_cpy.pop()
        elif c == 1:
            p1_cpy.pop()

        total_genes = len(p1_cpy) + len(p2_cpy)

    if total_genes == child_len:

        for gene in p1_cpy:
            child.append(gene)
        for gene in p2_cpy:
            child.append(gene)

    return child


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


def product(parent_1, parent_2):
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


def product_2(parent_1, parent_2):
    maximum_length = len(parent_1) + len(parent_2)
    child_length = int((len(parent_1) + len(parent_2)) / 2)

    if maximum_length >= 5:
        maximum_length = 5

    if child_length < maximum_length:
        child_length += random.randint(0, 1)

    child = []

    i = 0
    j = 0
    for n in range(0, child_length):
        r = random.randint(0, 1)

        if r == 0:
            if i < len(parent_1):
                child.append(parent_1[i])
            i += 1

        elif r == 1:
            if j < len(parent_2):
                child.append(parent_2[j])
            j += 1

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

        c = product(parent_1.get_chromosome(), parent_2.get_chromosome())
        c = mutate(c)

        child = Individual(length=len(c))
        child.set_chromosome(c)

        new_population.append(child)

    return new_population
