import random


def uniform_crossover_diff(p1_chromosome, p2_chromosome):
    """Uniform crossover when the length of the parents are unequal.

    Takes the values from the parents and randomly distribute them
    between the offsprings. The size of the offsprings equals the size
    of the parents.

    Args:
        p1_chromosome: The first parent, a list of numbers.
        p2_chromosome: The second parent, A list of numbers.
    Returns:
        Two lists of numbers which represent the offspring of
        the two parents.
    """
    if len(p1_chromosome) > len(p2_chromosome):
        long_parent = p1_chromosome
        short_parent = p2_chromosome
    else:
        long_parent = p2_chromosome
        short_parent = p1_chromosome

    c1_chromosome = []
    c2_chromosome = []

    for i in range(len(short_parent)):

        gene_1 = []
        gene_2 = []
        for j in range(8):
            flip = random.randint(0, 1)

            if flip == 1:
                gene_1.append(long_parent[i][j])
                gene_2.append(short_parent[i][j])
            else:
                gene_1.append(short_parent[i][j])
                gene_2.append(long_parent[i][j])

        c1_chromosome.append(gene_1)
        c2_chromosome.append(gene_2)

    for i in range(len(short_parent), len(long_parent)):
        gene_1 = []
        for j in range(8):
            gene_1.append(long_parent[i][j])

        c1_chromosome.append(gene_1)

    return c1_chromosome, c2_chromosome


def uniform_crossover(p1_chromosome, p2_chromosome):
    """Uniform crossover between two parents to produce two offspring.

    Takes all the values from the parents and randomly split them
    between the offsprings. If the chromosomes have different lengths
    another similar method is used.

    Args:
        p1_chromosome: The first parent, a list of numbers.
        p2_chromosome: The second parent, A list of numbers.
    Returns:
        Two lists of numbers which represent the offspring of
        the two parents.
    """
    if len(p1_chromosome) != len(p2_chromosome):
        return uniform_crossover_diff(p1_chromosome, p2_chromosome)

    c1_chromosome = []
    c2_chromosome = []

    for i in range(len(p1_chromosome)):
        flip = random.randint(0, 1)

        if flip == 1:
            c1_chromosome.append(p1_chromosome[i])
            c2_chromosome.append(p2_chromosome[i])
        else:
            c1_chromosome.append(p2_chromosome[i])
            c2_chromosome.append(p1_chromosome[i])

    return c1_chromosome, c2_chromosome
