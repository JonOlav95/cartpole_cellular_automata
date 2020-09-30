class Individual:

    """ An individual is also referred to as a "solution".

    A individual consists of a chromosome. A chromosome consists
    of genes.

    In our case the genes are CA rules, and the chromosome is a
    sequence of these rules. The is between 1-5 in length.
    """

    def __init__(self, length=0):

        self.__chromosome = []
        self.reward = 0
        self.length = length
        self.parent_times = 0

    def set_reward(self, reward):
        self.reward = reward

    def append_gene(self, gene):
        self.__chromosome.append(gene)

    def get_chromosome(self):
        return self.__chromosome

    def set_chromosome(self, chromosome):
        self.__chromosome = chromosome