import numpy as np


def ca_generate(obs, ca_range):
    """Arithmetically generates the first row in the CA board

    Arguments:
        obs: The observation. Is a list of numbers.
        ca_range: The CA range which decides where the initial 1s are placed.

    Returns:
        The first row of the CA.
    """
    cart_position = []
    cart_velocity = []
    pole_angle = []
    pole_velocity = []

    for i in range(-3, 3):
        cart_position.append(ca_range[0] * i)
        cart_velocity.append(ca_range[1] * i)
        pole_angle.append(ca_range[2] * i)
        pole_velocity.append(ca_range[3] * i)

    ca_cut = [cart_position, cart_velocity, pole_angle, pole_velocity]

    filler_len = 10
    ca_arr_gen = [0] * (len(obs) * 8 + ((len(obs) - 1) * filler_len))

    j = 0

    for i in range(0, len(obs)):

        if i != 0:
            j = (i - 1) * (filler_len + 8) + 8
            for n in range(filler_len):
                ca_arr_gen[j + n] = 0

        j = i * (filler_len + 8)

        if obs[i] <= ca_cut[i][0]:
            ca_arr_gen[j] = 1

        elif obs[i] >= ca_cut[i][len(ca_cut[i]) - 1]:
            ca_arr_gen[j + 7] = 1

        else:
            for n in range(1, 7):

                if ca_cut[i][n - 1] <= obs[i] <= ca_cut[i][n]:
                    ca_arr_gen[n + j] = 1
                    break

    return ca_arr_gen


def map_rule(rule_ids):
    """Maps the ruleset to their binary meaning.

    Arguments:
        rule_ids: A set of rules. Of the type list.

    Returns:
        Returns a list of directories. A directory contains the all the possible patterns
        and whether or not the rule activates on the pattern. It also includes the name of the rule
    """
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
        mapping["name"] = "Rule %d" % rule_id
        mapped_arr.append(mapping)

    return mapped_arr


def iterate(board, rule):
    board = np.pad(board, (1, 1), "constant", constant_values=(0, 0))
    new_board = np.zeros_like(board)

    for i in range(1, board.shape[0] - 1):
        side_step = tuple(board[i - 1:i + 2])
        new_board[i] = rule[side_step]

    return new_board[1:-1]


def converge_ca(initial_board, solution, num_iterations=100):
    """Converges the CA to find the output.

    Arguments:
        initial_board: The first row of the CA.
        solution: The list of rules in the directory form created by the mapped function.
        num_iterations: The height of the CA.

    Returns:
        All the rows in the CA.
    """
    board = initial_board
    rows = [board]

    # Keeps the height consistent regardless of ruleset size.
    num_iterations = int(num_iterations / len(solution))

    for i in range(num_iterations):
        for rule in solution:
            board = iterate(board, rule)
            rows.append(board)

    rows = np.array(rows)
    return rows


def converge_action(initial_board, individual):
    """Finds the action this step.

    Arguments:
        initial_board: The first row of the CA. A list of integers.
        individual: The solution. Of the type object Individual

    Returns:
        0 or 1.
    """
    solution = individual.chromosome

    mapped = map_rule(solution)
    board_outer = converge_ca(initial_board, mapped)

    if sum(board_outer[len(board_outer) - 1]) > len(board_outer[len(board_outer) - 1]) / 2:
        return 1

    return 0
