#!bin/usr/python3

import numpy as np
from SSA import SSA




def build_model():
    '''Builds the Predator Prey model'''
    stoch = np.array([[1, -1, -1, 0], [0, 0, 1, -1]])

    x_0 = [32,16]

    def props(x):
    	return np.array([x[0]*0.3,x[0]*x[1]*0.01,x[0]*x[1]*0.01,x[1]*0.3])

    return stoch,props,x_0


def arrange_into_bins(states,bin_dict,times):
    for idx,time in enumerate(times):
        #get index in bin array
        bin_dict[round(time,1)].append(states[idx])
    return bin_dict





def main():
    #read the input and initialize the seed aswell as the number of simulations
    with open('Input.txt','r') as input_1:
        seed = input_1.readline()
        n = input_1.readline()
    #set seed
    np.random.seed(int(seed))

    bins = np.arange(0,30.1,0.1)
    bins = [round(bin,1) for bin in bins]
    #create dictionary to store the values
    bin_dict = {bin:[] for bin in bins}
    bin_dict_1 = bin_dict.copy()
    bin_dict_2 = bin_dict.copy()

    stoch,props,x_0 = build_model()
    t_final = 30

    #execute the SSA n times and save time steps and status of state A
    for n_i in range(0,int(n)):
        states,times = SSA(stoch,props,x_0,t_final)
        bin_dict_1 = arrange_into_bins(states[0],bin_dict_1,times)
        bin_dict_2 = arrange_into_bins(states[1],bin_dict_2,times)
        #rearrange time points/states into 0.1 bins
        flattened_states_1 = []
        flattened_states_2 = []
        for bin in bins:
            #flatten the dictionaries so that they can be printed
            flattened_states_1.extend(bin_dict_1[bin])
            flattened_states_2.extend(bin_dict_2[bin])

        with open(f"Exc5Task3bTraj{n_i+1}Timed.txt","w") as output:
            output.write(",".join([str(bin) for bin in bins]))
            output.write("\n")
            output.write(",".join([str(state) for state in flattened_states_1]))
            output.write("\n")
            output.write(",".join([str(state) for state in flattened_states_2]))












if __name__ == "__main__":
    main()
