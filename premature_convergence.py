

def judgement_day(population):
    """Judgement day used to reset the majority of the population to avoid premature convergence.

    Checks for the amount of unique genes in a population. If the amount of unique genes is less
    than a certain threshold, judgement day should be applied.
    Judgement day can be performed in several different way, the responsibility of performing judgement day
    does not fall on this method. However, the most common way to perform judgement day is to randomize every
    individual except the one with the greatest fitness.

    Args:
        population: The population which will be checked for unique genes. Is a list of individuals.
    Returns:
        True if judgement day should be applied. False otherwise.
    """
    all_genes = set()

    total_genes = 0
    for individual in population:
        total_genes += len(individual.chromosome)

        for gene in individual.chromosome:
            all_genes.add(gene)

    unique_genes = len(set(all_genes))
    ratio = unique_genes / total_genes
    print("Unique Genes Percentage: " + str(round(ratio * 100, 2)))

    if ratio < 0.017:
        return True

    return False

