
def store_data(rew, folder):
    """Store the rewards for each generation in a text file.

    Args:
        rew: The reward for the generation.
        folder: the location of the folder where the text file is
    """
    filename = "ca_data/" + folder + "/_all_rewards.txt"

    with open(filename, mode="a") as file:
        file.write(str(int(rew)) + "\n")


# Function used to store data in textfiles
def store_data_all(pop, gen, rew, folder):
    """Store data of the generation in a text file.

    Stores the chromosomes and reward of each individual in the text file.

    Args:
        pop: The population for this generation.
        gen: The number of the generation.
        rew: The reward for the generation.
        folder: the location of the folder where the text file is
    """
    store_data(rew, folder)
    pop = sorted(pop, key=lambda x: x.reward, reverse=True)

    filename = "ca_data/" + folder + "/" + str(gen) + "_" + str(rew) + ".txt"

    with open(filename, mode="w") as file:
        file.write("Generation: " + str(gen) + "\tTotal Reward: " + str(rew) + "\n")

        for s in pop:
            length = len(str(s.chromosome_1))
            file.write("Reward: " + str(s.reward) + "   \tchromosome: " + str(s.chromosome_1))

            for i in range(30 - length):
                file.write(" ")

            file.write(str(s.chromosome_2) + "\n")
