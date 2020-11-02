import re
from individual import Individual
import matplotlib.pyplot as plt


# Messy functions occasionally used to store data

def tmp_func():
    individuals = []

    with open("data/52_26447.0.txt") as f:
        lines = f.readlines()

    for i in range(1, len(lines)):
        line = re.findall("[-+]?\d*\.\d+|\d+", lines[i])
        chromosome = list(map(int, line[1:len(line) - 4]))
        ca_cut = list(map(float, line[len(line) - 4:]))

        individual = Individual(len(chromosome))
        individual.chromosome_1 = chromosome
        individual.chromosome_2 = ca_cut

        individuals.append(individual)

    #np.random.shuffle(individuals)
    return individuals


# Function used to store data in textfiles
def store_data(pop, gen, rew):
    pop = sorted(pop, key=lambda x: x.reward, reverse=True)

    filename = "data/" + str(gen) + "_" + str(rew) + ".txt"

    with open(filename, mode="w") as file:
        file.write("Generation: " + str(gen) + "\tTotal Reward: " + str(rew) + "\n")

        for s in pop:
            length = len(str(s.chromosome_1))
            file.write("Reward: " + str(s.reward) + "   \tchromosome: " + str(s.chromosome_1))

            for i in range(30 - length):
                file.write(" ")

            file.write(str(s.chromosome_2) + "\n")


def visualize_board(board, title=None):
    plt.figure(figsize=(5, 2.5))
    plt.imshow(board, cmap="Greys")
    plt.axis("off")

    if title is not None:
        plt.title(title, fontsize=14)

    plt.show()
    plt.close()


def draw_ca(board_outer, mapped):

    name = ""
    for n in mapped:
        name += (n["name"]) + " "

    if sum(board_outer[len(board_outer) - 1]) > len(board_outer[len(board_outer) - 1]) / 2:
        name += "\n Action 1"
    else:
        name += "\n Action 0"

    visualize_board(board_outer, name)
