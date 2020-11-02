
def activation_func(value):
    """Activation function used within each neuron"""
    if value < 0:
        return 0

    return 1


class Neuron:
    """Neuron used as part of a neural network.

    Attributes:
        id: The identification of the neuron.
        value: The value of the neuron which is decided by the
        neural network, weights, and its bias.
        bias: The bias of the neuron which slightly adjusts the value.
        neighbours: The directory of neighbours which this neuron points to. Contains the neuron and the weight.
    """
    def __init__(self, id):
        """Inits the Neuron with an identification"""
        self.id = id
        self.value = 0
        self.bias = 0
        self.neighbours = {}

    def add_neighbour(self, to, weight):
        self.neighbours[to] = weight

    def forward(self, input_neuron=False):

        if not input_neuron:
            self.value += self.bias
            self.value = activation_func(self.value)

        for neighbour, weight in self.neighbours.items():
            neighbour.value += self.value * weight


class NeuralNetwork:
    """Neural network as a directed graph.
    Attributes:
        neurons: The list of neurons used within the neural network.
    """
    def __init__(self):
        self.neurons = []

    def add_edge(self, fr, to, weight):
        self.neurons[fr].add_neighbour(self.neurons[to], weight)

    def add_neuron(self, id, bias):
        neuron = Neuron(id)
        neuron.bias = bias
        self.neurons.append(neuron)

    def traverse(self, observations):
        for i in range(4):
            self.neurons[i].value = observations[i]
            self.neurons[i].forward(input_neuron=True)

        for i in range(4, len(self.neurons)):
            self.neurons[i].forward()

        return self.neurons[len(self.neurons) - 1].value


def init_neural_network(weights, bias):
    """Initiates a neural network.

    The neural network size is currently static and is not changeable by arguments.

    Args:
        weights: All the weights connected to the edges from top left to bottom right.
        bias: The bias of each neuron from top left to bottom right.

    Returns:
        A NeuralNetwork object adjusted with the arguments.
    """
    neural_network = NeuralNetwork()
    total_neurons = 17
    total_inputs = 4
    total_outputs = 1
    layer_length = 6
    n = 0

    for i in range(total_neurons):
        neural_network.add_neuron(i, bias[i])

    for i in range(total_inputs):
        for j in range(layer_length):
            neural_network.add_edge(i, j + total_inputs, weights[n])
            n += 1

    for i in range(total_inputs, total_inputs + layer_length):
        for j in range(total_inputs + layer_length, total_inputs + layer_length * 2):
            neural_network.add_edge(i, j, weights[n])
            n += 1

    for i in range(total_neurons - total_outputs - layer_length, total_neurons - total_outputs):
        for j in range(total_neurons - total_outputs, total_neurons):
            neural_network.add_edge(i, j, weights[n])
            n += 1

    return neural_network
