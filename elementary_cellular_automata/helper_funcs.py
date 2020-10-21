import random
from elementary_cellular_automata.individual import Individual


def initial_population():
    """Initiates a population of individuals with random chromosomes.

    Returns:
        A list of the object Individual.
    """
    individuals = []

    for j in range(100):

        sequence_size = random.randint(2, 5)
        individual = Individual(length=sequence_size)

        for i in range(sequence_size):

            gene = random.randint(0, 255)
            individual.chromosome.append(gene)

        individual.chromosome_ca = generate_ca_cut()
        individuals.append(individual)

    return individuals


def generate_individual():
    """Creates a sequence of rule sets and pack it into the object Individual.

    An Individual consists of two chromosomes. The first chromosome consists of
    CA rules. The second chromosome consists of the ranges used within the CA.

    Returns:
        The object Individual.
    """
    size = random.randint(2, 5)
    individual = Individual(length=size)

    for i in range(size):
        gene = random.randint(0, 255)
        individual.chromosome.append(gene)

    individual.chromosome_ca = generate_ca_cut()

    return individual


def generate_ca_cut():
    """Creates the ranges used in the CA

    Returns:
        A list of four floats.
    """
    ca_cut = [0.0] * 4
    ca_cut[0] = random.randint(1, 800) / 1000
    ca_cut[1] = random.randint(1, 2000) / 1000
    ca_cut[2] = random.randint(1, 240) / 1000
    ca_cut[3] = random.randint(1, 1000) / 2000

    return ca_cut
