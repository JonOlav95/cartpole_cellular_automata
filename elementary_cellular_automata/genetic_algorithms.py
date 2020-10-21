from crossover import uniform_crossover
from elementary_cellular_automata.helper_funcs import generate_individual
from elementary_cellular_automata.individual import Individual
from elementary_cellular_automata.mutation import mutate, ca_mutate
from selection import wheel_selection


def random_offspring(parent_1, parent_2):
    """Used to check if the parents have identical genes.

    If the length is not equal, the parents can not have identical genes.
    If there is a gene in the first parent which is not in the second,
    the parents can not have identical genes.
    If both parents have a reward of 500, it is possible that this solution
    is 'perfect', therefore it might be part of the global optimum and should
    not be replaced by random offspring.

    Arguments:
        parent_1: The first parent, an object of the type Individual. The entire object is sent instead
        of just the chromosome, because the reward is relevant.
        parent_2: The second parent.

    Returns:
        A boolean stating whether or not random offspring should be created.
    """
    if len(parent_1.chromosome) != len(parent_2.chromosome):
        return False

    for gene in parent_1.chromosome:
        if gene not in parent_2.chromosome:
            return False

    if parent_1.reward == 500 and parent_2.reward == 500:
        return False

    return True


def create_random_offspring():
    """Creates two random offspring"""
    individual_1 = generate_individual()
    individual_2 = generate_individual()

    return individual_1, individual_2


def uniform_crossover_binary(p1, p2):
    """Translate the rules to binary and apply crossover.

    Arguments:
        p1: The chromosome of the first parent. Is a list of numbers.
        p2: The chromosome of the second parent. Is a list of numbers.

    Returns:
        Two new rule sets in base 10 value. Is two lists of numbers.
    """
    p1_binary = []
    p2_binary = []

    for rule_id in p1:
        p1_binary.append(list(map(int, format(rule_id, "#010b")[2:])))

    for rule_id in p2:
        p2_binary.append(list(map(int, format(rule_id, "#010b")[2:])))

    c1, c2 = uniform_crossover(p1_binary, p2_binary)

    for i in range(len(c1)):
        c1[i] = int("".join(str(x) for x in c1[i]), 2)

    for j in range(len(c2)):
        c2[j] = int("".join(str(x) for x in c2[j]), 2)

    return c1, c2


def generate(population):
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

    # Sort the population to find out which had the best performance
    population = sorted(population, key=lambda x: x.reward, reverse=True)
    total_remove = 94

    # Elitism
    new_population = population[:(len(population) - total_remove)]

    parent_1, parent_2 = wheel_selection(total_remove, population)

    for i in range(int(total_remove / 2)):

        if random_offspring(parent_1[i], parent_2[i]):
            individual_1, individual_2 = create_random_offspring()
        else:
            rule_1, rule_2 = uniform_crossover_binary(parent_1[i].chromosome, parent_2[i].chromosome)
            range_1, range_2 = uniform_crossover(parent_1[i].chromosome_ca, parent_2[i].chromosome_ca)

            mutate(rule_1)
            mutate(rule_2)

            ca_mutate(range_1)
            ca_mutate(range_2)

            individual_1 = Individual()
            individual_2 = Individual()

            individual_1.chromosome = rule_1
            individual_2.chromosome = rule_2

            individual_1.chromosome_ca = range_1
            individual_2.chromosome_ca = range_2

        new_population.append(individual_1)
        new_population.append(individual_2)

    return new_population
