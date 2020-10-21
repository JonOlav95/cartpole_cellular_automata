import random


def add_gene(child):
    """Adds a random gene to the individuals chromosome"""
    index = random.randint(0, len(child))
    gene = random.randint(0, 255)

    child.insert(index, gene)


def remove_gene(child):
    """Removes a random gene from the individual chromosome"""
    index = random.randint(0, len(child) - 1)
    child.pop(index)


def modify_gene(child):
    """Modify a random gene in the individuals chromosome"""
    m = random.randint(0, len(child) - 1)
    child[m] = random.randint(0, 255)


def mutate(child):
    """The individual has a chance of being mutated in three different ways"""
    mutate_chance = random.randint(0, 10)
    if mutate_chance != 0:
        return

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


def ca_mutate(ca_cut):
    """Mutation of the ca chromosome"""
    mutate_chance = random.randint(0, 10)

    if mutate_chance != 0:
        return ca_cut

    index = random.randint(0, 3)

    if index == 0:
        ca_cut[index] = random.randint(1, 800) / 1000
    elif index == 1:
        ca_cut[index] = random.randint(1, 2000) / 1000
    elif index == 2:
        ca_cut[index] = random.randint(1, 240) / 1000
    elif index == 3:
        ca_cut[index] = random.randint(1, 1000) / 2000

