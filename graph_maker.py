import matplotlib.pyplot as plt


i = 15
print(str(i))
name = "artifical_neural_network/data/data_" + str(7) + ".txt"
name_2 = "artifical_neural_network/data/data_" + str(13) + ".txt"

lines = open(name).read().split("\n")
lines_2 = open(name_2).read().split("\n")

x_arr = []
for i in range(1000):
    x_arr.append(i)

arr = []
arr_2 = []

for line in lines:
    arr.append(int(line))

for line in lines_2:
    arr_2.append(int(line))

plt.plot(arr)
plt.plot(arr_2)
plt.ylim(0, 50000)
plt.ylabel("Fitness")
plt.xlabel("Generation")
plt.show()
