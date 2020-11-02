# Function used to store data in textfiles
def store_data(rew):

    filename = "data/ca_8.txt"

    with open(filename, mode="a") as file:
        file.write(str(int(rew)) + "\n")
