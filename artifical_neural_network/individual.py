class Individual:
    """An Individual is synonymous with a solution in the population.

    Attributes:
        chromosome: The main chromosome which is a list of weights.
        bias_chromosome: The chromosome which is a list of biases.
        reward: The reward (fitness) the Individual obtained in the simulation.
    """

    def __init__(self):
        self.chromosome = []
        self.bias_chromosome = []
        self.reward = 0
