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
    #read the input and initialize the seed
    with open('Input2.txt','r') as input_1:
        seed = input_1.readline()

    #initialize the number of simulations and set the seed
    ns = [10,100,1000,10000]
    np.random.seed(int(seed))

    stoch,props,x_0 = build_model()
    t_final = 10

    means = []
    #for each number of simulations store all values of A at T=10
    for n in ns:
        x_a = []
        for n_i in range(0,int(n)):
            states,times = SSA(stoch,props,x_0,t_final)
            x_a.append(states[0][-1])
        #compute mean of A at T=10
        means.append(np.mean(x_a))
    #save means to outputfile
    with open(f"Exc4Task2b.txt","w") as output:
        output.write(",".join([str(round(mean,2)) for mean in means]))








if __name__ == "__main__":
    main()
