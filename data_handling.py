import re
from cellular_automata.individual import Individual


def tmp_func():
    individuals = []

    with open("data/52_26447.0.txt") as f:
        lines = f.readlines()

    for i in range(1, len(lines)):
        line = re.findall("[-+]?\d*\.\d+|\d+", lines[i])
        chromosome = list(map(int, line[1:len(line) - 4]))
        ca_cut = list(map(float, line[len(line) - 4:]))

        individual = Individual(len(chromosome))
        individual.chromosome = chromosome
        individual.chromosome_ca = ca_cut

        individuals.append(individual)

    #np.random.shuffle(individuals)
    return individuals


