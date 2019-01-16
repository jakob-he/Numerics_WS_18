#/bin/usr/python3
import numpy as np
import argparse
import math




def x(t_i,lam,delta):
    return lam/delta*(1-np.exp(-delta*t_i))

def likeli(t_i,y_i,lam,delta):
    x_ti = x(t_i,lam,delta)
    return ((x_ti^(y_i))*np.exp(-x_ti)))/(math.factorial(y_i))



def main():
    #read Input
    with open("Input.txt","r") as input:
        lam = input.readline()
        delta = input.readline()

    #set measurements and time
    Y = [108,108,101,108,109,91,108,97,92,98]
    t = 100


    #compute likelihood of the data
    likelihood = np.prod([likeli(t,y_i,lam,delta) for y_i in Y])
    print(likelihood)




if __name__ == "__main__":
    main()
