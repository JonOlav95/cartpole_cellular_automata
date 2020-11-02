class Individual:
    """ An individual is also referred to as a "solution".

    A individual consists of two chromosomes. A chromosome consists
    of genes.

    In our case the genes are CA rules, and the chromosome is a
    sequence of these rules. The is between 1-5 in length.
    """
    def __init__(self):
        self.chromosome_1 = []
        self.chromosome_2 = []
        self.reward = 0
