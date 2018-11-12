#!/usr/bin/python3
import numpy as np


def update_Reactions(x):
    r_1 = 10**-4
    r_2 = x[0] * 10**(-8)
    r_3 = x[0] * x[1] * 5 * 10**(-5)
    r_4 = x[1] * 3 * 10**(7) * 10**(-8)
    r_5 = x[1] * 0.3
    r_6 = x[2] * 10**(-8)
    return [r_1, r_2, r_3, r_4, r_5, r_6]


def get_S():
    return np.array([[1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0], [0, 0, 0, 0, 1, -1], [0, 0, 0, 1, 0, 0]])


def ssa(x_0: [int], t_0: int, t_final: int, s: np.array, sim_number: int=1, save_results=False):
    x = x_0
    t = t_0
    x_2s = []
    ts = []
    while(t < t_final):
        x_2s.append(x[1])
        ts.append(t)
        # get/update reactions
        reactions = update_Reactions(x)
        a_0 = sum(reactions)
        if a_0 == 0:
            t = t_final
            break
        taus = np.random.random_sample(2,)
        t_delta = (1 / a_0) * np.log(1 / taus[0])
        if (t + t_delta) > t_final:#
            t = t_final
            break
        t = t + t_delta
        b = [0] + reactions
        for j in range(0, len(reactions)):
            if sum(b[:j]) < (a_0 * taus[1]) <= sum(b[:j+1]):
                x = np.add(x, s[:, j].flatten())
                break

    ts.append(t)
    # save results to txt file
    if save_results:
        with open(f'traj{sim_number+1}.txt', 'w') as output:
            output.write(",".join([str(t) for t in ts]))
            output.write("\n")
            output.write(",".join([str(x_2) for x_2 in x_2s]))

    return x, x_2s, ts


def main():
    with open('Input.txt', 'r') as input:
        seed = input.readline()
        n = input.readline()

    np.random.seed(int(seed))
    s = get_S()
    x_0 = [10000, 5, 0, 0]
    t_0 = 0
    t_final = 10

    results = [ssa(x_0, t_0, t_final, s, sim_number=n_i, save_results=True)
               for n_i in range(0, int(n))]

    x, x_2, ts = results[0]
    print(x_2)


if __name__ == "__main__":
    main()
