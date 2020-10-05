import random


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
