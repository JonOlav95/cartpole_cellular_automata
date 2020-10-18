import random


# Adds a random gene to the individuals chromosome
def add_gene(child):
    index = random.randint(0, len(child))
    gene = random.randint(0, 255)

    child.insert(index, gene)


# Removes a random gene from the individual chromosome
def remove_gene(child):
    index = random.randint(0, len(child) - 1)
    child.pop(index)


# Modify a random gene in the individuals chromosome
def modify_gene(child):
    m = random.randint(0, len(child) - 1)
    child[m] = random.randint(0, 255)


# The individual has a chance of being mutated in three different ways
def mutate(child):
    mutate_chance = random.randint(0, 20)
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


# Mutation of the ca chromosome
def ca_mutate(ca_cut):
    mutate_chance = random.randint(0, 20)

    if mutate_chance != 0:
        return ca_cut

    index = random.randint(0, 3)

    if index == 0:
        ca_cut[index] = random.randint(1, 800) / 2000
    elif index == 1:
        ca_cut[index] = random.randint(1, 2000) / 2000
    elif index == 2:
        ca_cut[index] = random.randint(1, 240) / 2000
    elif index == 3:
        ca_cut[index] = random.randint(1, 3000) / 4000

    return ca_cut