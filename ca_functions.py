from past.builtins import xrange


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


def rule_to_bin(rule):
    bin_rule = bin(rule)[2:]
    missing = 8 - len(bin_rule)
    bin_rule = "0" * missing + bin_rule

    bin_rule_arr = []
    for i in range(len(bin_rule)):
        bin_rule_arr.append(int(bin_rule[i]))

    return bin_rule_arr


def rules_to_action(ca_arr_n, solution):
    chromosome = solution.get_chromosome()

    bin_rule = []
    for j in range(len(chromosome)):
        bin_rule.append(rule_to_bin(chromosome[j]))

    next_step = [0] * len(ca_arr_n)

    for k in range(10):
        for j in range(len(chromosome)):

            for n in xrange(len(next_step)):
                next_step[n] = 0

            for i in range(len(ca_arr_n)):
                pattern = ""

                if i == 0:
                    pattern += str(ca_arr_n[len(ca_arr_n) - 1])
                else:
                    pattern += str(ca_arr_n[i - 1])

                pattern += str(ca_arr_n[i])

                if i == len(ca_arr_n) - 1:
                    pattern += str(ca_arr_n[0])
                else:
                    pattern += str(ca_arr_n[i + 1])

                if pattern == "111":
                    next_step[i] = bin_rule[j][0]
                elif pattern == "110":
                    next_step[i] = bin_rule[j][1]
                elif pattern == "101":
                    next_step[i] = bin_rule[j][2]
                elif pattern == "100":
                    next_step[i] = bin_rule[j][3]
                elif pattern == "011":
                    next_step[i] = bin_rule[j][4]
                elif pattern == "010":
                    next_step[i] = bin_rule[j][5]
                elif pattern == "001":
                    next_step[i] = bin_rule[j][6]
                elif pattern == "000":
                    next_step[i] = bin_rule[j][7]

            for n in xrange(len(ca_arr_n)):
                ca_arr_n[n] = next_step[n]

    if sum(ca_arr_n) > len(ca_arr_n) / 2:
        return 1

    return 0
