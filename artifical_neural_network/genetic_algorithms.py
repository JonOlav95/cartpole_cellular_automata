import random

from artifical_neural_network.helper_funcs import random_neural_network
from artifical_neural_network.individual import Individual
from crossover import uniform_crossover
from premature_convergence import judgement_day
from selection import wheel_selection, tournament_selection


def mutate(chromosome):
    """Mutates a chromosome.

    Args:
        chromosome: The list of numbers that will be mutated.

    Returns:
        A list of the same size which may or may not be mutated.
    """
    while True:
        chance = random.randint(0, 30)
        if chance == 0:
            index = random.randint(0, len(chromosome) - 1)
            addition = random.uniform(-0.5, 0.5)
            chromosome[index] += addition
            if chromosome[index] < -1:
                chromosome[index] = -1
            elif chromosome[index] > 1:
                chromosome[index] = 1

        elif chance == 1:
            index = random.randint(0, len(chromosome) - 1)
            weight = random.uniform(-1, 1)
            chromosome[index] = weight

        else:
            return chromosome



def survival(population):
    """Applies the evolutionary survival process to the population.

    A few select elites with the best reward (fitness) is automatically part of the next generation.
    From the population parents are selected to create offspring. The offspring will be part of
    the next generation. The parents will cease to exist unless they were part of the elite.
    Mutation is applied to the offspring, which has a chance of altering the chromosomes.

    Args:
        The population which is a list of the object Individual. The entire population just ran in
        the simulation and their reward (fitness) was stored.

    Returns:
        A new population which is a list of the object Individual. The new population is the next generation
        and consists of the elite from the previous population and offspring from the previous generation.
    """

    # Sort the population by its reward (fitness)
    population = sorted(population, key=lambda x: x.reward, reverse=True)
    total_remove = 94

    if judgement_day(population):
        new_population = [population[0]]

        for i in range(100 - len(new_population)):
            new_population.append(random_neural_network())

        return new_population

    # Elitism
    new_population = population[:(len(population) - total_remove)]

    #parent_1, parent_2 = tournament_selection(total_remove, population)

    parent_1, parent_2 = wheel_selection(total_remove, population)

    for i in range(int(total_remove / 2)):
        weight_1, weight_2 = uniform_crossover(parent_1[i].chromosome, parent_2[i].chromosome)
        bias_1, bias_2 = uniform_crossover(parent_1[i].bias_chromosome, parent_2[i].bias_chromosome)

        mutate(weight_1)
        mutate(weight_2)
        mutate(bias_1)
        mutate(bias_2)

        c1 = Individual()
        c2 = Individual()

        c1.chromosome = weight_1
        c1.bias_chromosome = bias_1

        c2.chromosome = weight_2
        c2.bias_chromosome = bias_2

        new_population.append(c1)
        new_population.append(c2)

    return new_population
