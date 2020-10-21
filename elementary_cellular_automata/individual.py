class Individual:
    """ An individual is also referred to as a "solution".

    A individual consists of two chromosomes. A chromosome consists
    of genes.

    In our case the genes are CA rules, and the chromosome is a
    sequence of these rules. The is between 1-5 in length.
    """
    def __init__(self, length=0):
        self.chromosome = []
        self.chromosome_ca = []
        self.reward = 0
        self.length = length
        self.parent_times = 0

    def set_reward(self, reward):
        self.reward = reward
