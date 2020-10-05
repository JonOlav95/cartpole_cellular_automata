from past.builtins import xrange
import numpy as np
import matplotlib.pyplot as plt
import time


def ca_generate(obs):
    cart_position = [-0.05, -0.02, 0.0, 0.02, 0.05]
    cart_velocity = [-0.1, -0.05, 0.0, 0.05, 0.1]
    pole_angle = [-0.24, -0.12, 0.0, 0.12, 0.24]
    pole_velocity = [-0.1, -0.05, 0.0, 0.05, 0.1]

    ca_cut = [cart_position, cart_velocity, pole_angle, pole_velocity]

    repeat = 4
    obs_space = len(cart_position) + 1
    zero_space = 5
    pattern_length = (len(obs) * obs_space) + ((len(obs) - 1) * zero_space)
    ca_arr_gen = [0] * pattern_length * repeat

    for n in range(0, repeat):
        for i in range(0, len(obs)):

            j = i * (obs_space + zero_space) + (n * pattern_length)

            if obs[i] <= ca_cut[i][0]:
                ca_arr_gen[j] = 1

            elif obs[i] >= ca_cut[i][len(ca_cut[i]) - 1]:
                ca_arr_gen[j + 5] = 1

            else:
                for k in range(1, 5):

                    if ca_cut[i][k - 1] <= obs[i] <= ca_cut[i][k]:
                        ca_arr_gen[k + j] = 1

            if n != repeat - 1 and i != len(obs) - 1:
                for k in range(0, zero_space):
                    ca_arr_gen[j + obs_space + k] = 0

    return ca_arr_gen


def map_rule(rule_ids):
    mapped_arr = []

    input_patterns = [
        (1, 1, 1),
        (1, 1, 0),
        (1, 0, 1),
        (1, 0, 0),
        (0, 1, 1),
        (0, 1, 0),
        (0, 0, 1),
        (0, 0, 0)
    ]

    for rule_id in rule_ids:
        outputs = list(map(int, format(rule_id, "#010b")[2:]))
        mapping = dict(zip(input_patterns, outputs))
        mapping["name"] = "Rule %d" % (rule_id)
        mapped_arr.append(mapping)

    return mapped_arr


def iterate(board, rule):
    board = np.pad(board, (1, 1), "constant", constant_values=(0, 0))
    new_board = np.zeros_like(board)
    for i in range(1, board.shape[0] - 1):
        side_step = tuple(board[i - 1:i + 2])
        new_board[i] = rule[side_step]
    return new_board[1:-1]


def converge_ca(initial_board, solution, num_iterations=5):
    board = initial_board
    rows = [board]

    num_iterations = int(num_iterations/len(solution))

    for i in range(num_iterations):
        for rule in solution:
            board = iterate(board, rule)
            rows.append(board)

    rows = np.array(rows)
    return rows


def visualize_board(board, title=None):
    plt.figure(figsize=(5, 2.5))
    plt.imshow(board, cmap="Greys")
    plt.axis("off")
    if title is not None:
        plt.title(title, fontsize=14)
    plt.show()
    plt.close()


# TODO: Change func name
def generate_action(initial_board, individual):
    solution = individual.get_chromosome()

    mapped = map_rule(solution)

    board_outer = converge_ca(initial_board, mapped)

    '''
    name = ""
    for n in mapped:
        name += (n["name"]) + " "

    visualize_board(board_outer, name)
    '''

    if sum(board_outer[len(board_outer) - 1]) > len(board_outer[len(board_outer) - 1]) / 2:
        return 1

    return 0
