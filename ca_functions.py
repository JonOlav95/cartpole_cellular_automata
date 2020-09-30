# Lacks comments

def ca_generate(obs):
    cart_position = [-0.05, -0.02, 0.0, 0.02, 0.05]
    cart_velocity = [-0.1, -0.05, 0.0, 0.05, 0.1]
    pole_angle = [-0.24, -0.12, 0.0, 0.12, 0.24]
    pole_velocity = [-0.1, -0.05, 0.0, 0.05, 0.1]

    ca_cut = [cart_position, cart_velocity, pole_angle, pole_velocity]

    ca_arr_gen = [0] * len(obs) * 6

    for i in range(0, len(obs)):

        j = i * 6

        if obs[i] <= ca_cut[i][0]:
            ca_arr_gen[j] = 1

        elif obs[i] >= ca_cut[i][len(ca_cut[i]) - 1]:
            ca_arr_gen[j + 5] = 1

        else:
            for n in range(1, 5):

                if ca_cut[i][n - 1] <= obs[i] <= ca_cut[i][n]:
                    ca_arr_gen[n + j] = 1



    tmp = sum(ca_arr_gen)

    if tmp < 4:
        print(str(tmp))

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

    for j in range(len(chromosome)):

        bin_rule = rule_to_bin(chromosome[j])
        next_step = [0] * 24

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
                next_step[i] = bin_rule[0]
            elif pattern == "110":
                next_step[i] = bin_rule[1]
            elif pattern == "101":
                next_step[i] = bin_rule[2]
            elif pattern == "100":
                next_step[i] = bin_rule[3]
            elif pattern == "011":
                next_step[i] = bin_rule[4]
            elif pattern == "010":
                next_step[i] = bin_rule[5]
            elif pattern == "001":
                next_step[i] = bin_rule[6]
            elif pattern == "000":
                next_step[i] = bin_rule[7]

        ca_arr_n = next_step

    if sum(ca_arr_n) > len(ca_arr_n) / 2:
        return 1

    return 0
