#!bin/usr/python3
import numpy as np
import matplotlib.pyplot as plt

def implicit_euler(func,intervall_start,intervall_end,stepsize):
    x_t = 0
    approximations = [x_t]
    for step in np.arange(intervall_start,intervall_end,stepsize):
        #fixed point iteration
        tolerance = 1
        approximation = x_t
        while tolerance > 1e-12:
            new_x_t_delta = x_t + stepsize*f(step+stepsize,approximation)
            tolerance = abs(new_x_t_delta-approximation)
            approximation = new_x_t_delta
        x_t = approximation
        approximations.append(x_t)
    return approximations


def f(t,x_t):
    return 0.5*(200*np.exp(-0.5*t))-0.3*x_t

def save_to_txt(states,times,path):
    with open(path,"w") as output:
        output.write(",".join([str(time) for time in times]))
        output.write("\n")
        output.write(",".join([str(round(state,2)) for state in states]))



def main():
    stepsizes = [0.1,0.25,0.5]
    means = []
    intervall_start = 0
    intervall_end = 24
    for stepsize in stepsizes:
        approximations = implicit_euler(f,intervall_start,intervall_end,stepsize)
        ts = np.arange(intervall_start,intervall_end+stepsize,stepsize)
        real_xs = [(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t))) for t in ts]
        means.append(np.mean(abs(np.subtract(real_xs,approximations))))

    plt.loglog(stepsizes,stepsizes,color='red', label=r'$\Delta$ t')
    plt.loglog(stepsizes,means,linestyle=':',marker='o', label = 'Implicit Euler')
    plt.title('Average Error: Implicit Euler')
    plt.ylabel('Average Error')
    plt.xlabel('Stepsize')
    plt.yticks()
    plt.legend()
    plt.savefig('Exc7Task3b.png')











if __name__ == "__main__":
    main()
