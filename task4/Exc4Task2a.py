#!bin/usr/python3

import numpy as np
from SSA import SSA




def build_model():
    '''Builds the Boomerang process model'''
    stoch = np.array([[1, 0 ,-1], [0, 1, -1]])

    x_0 = [10,10]

    def props(x):
    	return np.array([1,1,0.01*x[0]*x[1]])

    return stoch,props,x_0








def main():
    #read the input and initialize the seed aswell as the number of simulations
    with open('Input1.txt','r') as input_1:
        seed = input_1.readline()
        n = input_1.readline()
    #set seed
    np.random.seed(int(seed))

    stoch,props,x_0 = build_model()
    t_final = 10

    #execute the SSA n times and save time steps and status of state A
    for n_i in range(0,int(n)):
        states,times = SSA(stoch,props,x_0,t_final)
        with open(f"Exc4Task2aTraj{n_i+1}.txt","w") as output:
            output.write(",".join([str(round(time,2)) for time in times]))
            output.write("\n")
            output.write(",".join([str(state) for state in states[0]]))












if __name__ == "__main__":
    main()
