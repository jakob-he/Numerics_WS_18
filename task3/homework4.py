#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt

def update_Reactions(x):
    '''
    Returns a list of values that correspond to the results
    of the reactions given x.
    '''
    r_1 = 10**(-4)
    r_2 = x[0] * 10**(-8)
    r_3 = x[0] * x[1] * 5 * 10**(-5)
    r_4 = x[1] * 3 * 10**(7) * 10**(-8)
    r_5 = x[1] * 0.3
    r_6 = x[2] * 10**(-8)
    return [r_1, r_2, r_3, r_4, r_5, r_6]


def get_S():
    '''Constructs the stochiometric matrix'''
    return np.array([[1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0], [0, 0, 0, 0, 1, -1], [0, 0, 0, 1, 0, 0]])


def ssa(x_0: [int], t_0: int, t_final: int, s: np.array, sim_number: int=1, save_results=False):
    '''Performs the stochastic simulation algorithm with the given input parameters'''

    #initialize x,t and the lists for all x_2 values and ts
    x = x_0
    t = t_0
    x_2s = []
    ts = []
    while(t < t_final):
        #append new x_2 and t values
        x_2s.append(x[1])
        ts.append(t)
        # get/update reactions
        reactions = update_Reactions(x)
        #compute sum of the reactions
        a_0 = sum(reactions)
        #break the while loop if the sum is 0
        if a_0 == 0:
            t = t_final
            break
        #sample two values from a uniform distribution u ~ [0,1)
        taus = np.random.random(2,)
        #compute the incremental step
        t_delta = (1 / a_0) * np.log(1 / taus[0])
        #break the while loop if t is now larger than t final
        if (t + t_delta) > t_final:#
            t = t_final
            break
        t = t + t_delta
        b = [0] + reactions
        #choose j such that the sum of all reactions up to
        #reaction j is smaller than a_0*tau_1 which in turn is
        #less than the sum of all reactions including j
        for j in range(0, len(reactions)):
            if sum(b[:j]) < (a_0 * taus[1]) <= sum(b[:j+1]):
                #add the jth column of the sociometric matrix to x
                x = np.add(x, s[:, j].flatten())
                break
    #append final t value
    ts.append(t)
    # save results to txt file
    if save_results:
        with open(f'traj{sim_number+1}.txt', 'w') as output:
            output.write(",".join([str(t) for t in ts]))
            output.write("\n")
            output.write(",".join([str(x_2) for x_2 in x_2s]))
    return x, x_2s, ts


def main():

    #Subtask A
    x_0 = [10000, 5, 0, 0]
    t_0 = 0
    t_final = 10
    with open('Input.txt', 'r') as input:
        seed = input.readline()
        n = input.readline()

    np.random.seed(int(seed))
    s = get_S()
    x_0 = [10000, 5, 0, 0]
    t_0 = 0
    t_final = 10

    #results = [ssa(x_0, t_0, t_final, s, sim_number=n_i, save_results=True) for n_i in range(0, int(n))]

    #Subtask B
    n = 1000

    results = [ssa(x_0, t_0, t_final, s) for n_i in range(0, int(n))]

    x_2s = [result[0][1] for result in results]
    u, inv = np.unique(x_2s, return_inverse=True)
    counts = np.bincount(inv)

    #probability that infection is still ongoing
    prob_1 = counts[1]/sum(counts)

    print(f'Probability that the infections is still on going at T=10: {prob_1}')
    plt.figure(0)
    plt.bar(u, counts, width=0.5)
    plt.xticks(np.arange(0,6,1))
    plt.title('Distribution of x_2 values for N=1000')
    plt.savefig('x_2.png')


    #Subtask C
    x_4s = [result[0][3] for result in results]

    #average and std of the number of people who died
    average = np.average(x_4s)
    std = np.std(x_4s)

    print(f'Average (+-std) number of who died by T=10: {average}+-{std}')

    u, inv = np.unique(x_4s, return_inverse=True)
    counts = np.bincount(inv)



    plt.figure(1)
    plt.bar(u, counts, width=0.5)
    plt.xticks(np.arange(0,6,1))
    plt.title('Distribution of x_2 values for N=1000')
    plt.savefig('x_4.png')

if __name__ == "__main__":
    main()
