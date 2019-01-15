#!bin/usr/python3

import numpy as np
from SSA import SSA
import matplotlib.pyplot as plt




def build_model():
    '''Builds the Stögl model'''
    stoch = np.array([[1, -1, 1, -1]])

    x_0 = [40]

    def props(x):
    	return np.array([0.15*x[0]**2-x[0],0.0015*(x[0]**3-3*x[0]**2+2*x[0]),20,3.5*x[0]])

    return stoch,props,x_0








def main():
    #SUBTASK a
    #set seed and number of simulations based on input
    with open('Input1.txt','r') as input_1:
        seed = input_1.readline()
        n = input_1.readline()

    np.random.seed(int(seed))

    stoch,props,x_0 = build_model()
    t_final = 5

    #Similar to 2a: The state population and time steps are written to an outputfile
    for n_i in range(0,int(n)):
        states,times = SSA(stoch,props,x_0,t_final)
        with open(f"Exc4Task3Traj{n_i+1}.txt","w") as output:
            output.write(",".join([str(round(time,2)) for time in times]))
            output.write("\n")
            output.write(",".join([str(state) for state in states[0]]))

    #SUBTASK b
    n = 200

    #store all values of x_1 at T=5 for 200 simulations
    x_1 = []
    for n_i in range(0,n):
        states,times = SSA(stoch,props,x_0,t_final)
        x_1.append(states[0][-1])

    #compute the sample mean
    sample_mean = np.mean(x_10)
    
    #plot the histogram of x_1 values at T=5 and mark the sample mean
    plt.hist(x_1,bins=range(max(x_1)),density=True)
    plt.annotate("Sample mean",arrowprops={'arrowstyle':'->'},xytext=(sample_mean,0.12),xy=(sample_mean,0.1))
    plt.xlabel("Population of X_1")
    plt.ylabel("Probability of Observing X_1 at time T=5")
    plt.savefig("Exc4Task3b.png")










if __name__ == "__main__":
    main()
