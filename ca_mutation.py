import random


def ca_mutate(ca_cut):
    mutate_chance = random.randint(0, 4)

    if mutate_chance != 0:
        return ca_cut

    index = random.randint(0, 3)

    if index == 0:
        ca_cut[index] = random.randint(0, 80) / 100
    elif index == 1:
        ca_cut[index] = random.randint(0, 200) / 100
    elif index == 2:
        ca_cut[index] = random.randint(0, 24) / 100
    elif index == 3:
        ca_cut[index] = random.randint(0, 300) / 100

    return ca_cut
