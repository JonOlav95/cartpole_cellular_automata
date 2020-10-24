

def judgement_day(population):

    all_genes = set()

    total_genes = 0
    for individual in population:
        total_genes += len(individual.chromosome)

        for gene in individual.chromosome:
            all_genes.add(gene)

    unique_genes = len(set(all_genes))
    ratio = unique_genes / total_genes
    print("Unique Genes Percentage: " + str(round(ratio * 100, 2)))

    if ratio < 0.015:
        return True

    return False

