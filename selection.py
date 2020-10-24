import numpy.random as npr
import random
from operator import attrgetter


def wheel_selection(total_offspring, population):
    """Wheel selection used to select parents.

    High reward parents have a higher chance of being chosen.

    Args:
        total_offspring: The total amount of offspring the new population requires.
        population: The population of potential parents.
    """
    max_reward = sum([c.reward for c in population])
    selection_prob = [c.reward / max_reward for c in population]

    parents_1 = []
    parents_2 = []

    for i in range(int(total_offspring / 2)):

        p1 = None
        p2 = None

        while p1 == p2:
            p1 = population[npr.choice(len(population), p=selection_prob)]
            p2 = population[npr.choice(len(population), p=selection_prob)]

        parents_1.append(p1)
        parents_2.append(p2)

    return parents_1, parents_2


def tournament_selection(total_offspring, population):

    n = 15
    parents = []

    for i in range(total_offspring):
        contestants = random.sample(population, n)
        winner = max(contestants, key=attrgetter("reward"))
        parents.append(winner)

    parents_1 = parents[0:int(total_offspring/2)]
    parents_2 = parents[int(total_offspring/2):total_offspring]

    return parents_1, parents_2


