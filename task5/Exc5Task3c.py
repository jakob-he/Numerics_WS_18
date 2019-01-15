#!bin/usr/python3

import numpy as np
from SSA import SSA
import matplotlib.pyplot as plt




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
    #set seed and number of simulations
    np.random.seed(3)
    n = 300

    bins = np.arange(0,30.1,0.1)
    bins = [round(bin,1) for bin in bins]
    #create dictionary to store the values
    bin_dict = {bin:[] for bin in bins}


    stoch,props,x_0 = build_model()
    t_final = 30

    #execute the SSA n times and save time steps and status of state A
    for n_i in range(0,n):
        states,times = SSA(stoch,props,x_0,t_final)
        bin_dict = arrange_into_bins(states[0],bin_dict,times)

    mean = [np.mean(items) for key,items in bin_dict.items()]
    std = [np.std(items) for key,items in bin_dict.items()]
    plt.plot(bins,mean, color="k", label="sample mean")
    plt.plot(bins,np.add(mean,std),color="r", label="sample mean +- std", linewidth=1)
    plt.plot(bins,np.subtract(mean,std),color="r", linewidth=1)
    plt.title("Predator-Prey Simulations")
    plt.xlabel("time")
    plt.legend()
    plt.savefig("Exc5Task3cfig.png")














if __name__ == "__main__":
    main()
