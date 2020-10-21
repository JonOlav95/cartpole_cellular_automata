import random
from artifical_neural_network.individual import Individual


def random_neural_network():
    """Creates a neural network with random weights and biases

    Returns:
        The object Individual.
    """
    individual = Individual()

    for n in range(17):
        bias = random.uniform(-1, 1)
        individual.bias_chromosome.append(bias)

    for j in range(66):
        weight = random.uniform(-1, 1)

        individual.chromosome.append(weight)

    return individual


def init_population():
    """Initiates a population of individuals with random weights and biases

    Returns:
        A list of the object Individual.
    """
    population = []

    for i in range(100):
        individual = random_neural_network()
        population.append(individual)

    return population
