'''Script used to compute the trajectory of a poission process'''
import matplotlib.pyplot as plt
import numpy as np


def generate_Xt(t:int):
    '''
    Returns Xt with lambda equal to 2.45635 given that the
    expected value of a possion process at a specific time step
    is lambda*t.
    '''
    return(10+(2.45635*t))

def exp_func(t:int):
    '''returns incremental step for previous X and lambda equal to 2.45635'''
    return(10+(2.45635*np.exp(-2.45635*t)))


def main():

    #compute trajectory
    trajectory = [generate_Xt(t)-generate_Xt(t-1) for t in range(0,3000)]

    #The overlay of a exponential distribution did not work for us
    #since every value for this lambda and this intervall of t was almost equal to 10.
    #Therefore the values couldnt be represented in the same scale as
    #the values of the incremental steps.

    #exp = [exp_func(t) for t in range(0,3000)]
    #plot the histogram with exponential dist
    plt.hist(trajectory,density=True)
    #plt.plot(exp)
    plt.show()

if __name__ == "__main__":
    main()
