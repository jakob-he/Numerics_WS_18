#!bin/usr/python3
import numpy as np
import matplotlib.pyplot as plt

def rectangle_rule(func,intervall_start,intervall_end,stepsize):
    sum = 0
    x_t = 0
    xs = [x_t]
    integral_t = 0
    for i in range(intervall_start,intervall_end):
        integral_delta_t = stepsize*func(intervall_start+i)
        x_t += integral_t + integral_delta_t
        integral_t = integral_delta_t
        xs.append(x_t)
    return xs


def f(t):
    return 0.5*(200*np.exp(-0.5*t))-0.3*(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t)))

def save_to_txt(states,times,path):
    with open(path,"w") as output:
        output.write(",".join([str(time) for time in times]))
        output.write("\n")
        output.write(",".join([str(round(state,2)) for state in states]))



def main():
    stepsize = 1
    intervall_start = 0
    intervall_end = 24
    xs = rectangle_rule(f,intervall_start,intervall_end,stepsize)
    real_xs = [(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t))) for t in range(0,intervall_end)]
    save_to_txt(xs,range(intervall_start,intervall_end),"Exc6Task3a.txt")












if __name__ == "__main__":
    main()
