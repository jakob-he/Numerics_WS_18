#!bin/usr/python3
import numpy as np
import matplotlib.pyplot as plt

def explicit_euler(func,intervall_start,intervall_end,stepsize):
    x_t = 0
    approximations = [x_t]
    for step in np.arange(intervall_start+stepsize,intervall_end+stepsize,stepsize):
        x_delta_t = x_t + stepsize*func(step,x_t)
        x_t = x_delta_t
        approximations.append(x_delta_t)
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
        approximations = explicit_euler(f,intervall_start,intervall_end,stepsize)
        ts = np.arange(intervall_start,intervall_end+stepsize,stepsize)
        real_xs = [(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t))) for t in ts]
        means.append(np.mean(abs(np.subtract(real_xs,approximations))))

    plt.loglog(stepsizes,stepsizes,color='red', label=r'$\Delta$ t')
    plt.loglog(stepsizes,means,linestyle=':',marker='o', label = 'Explicit Euler')
    plt.title('Average Error: Explicit Euler')
    plt.ylabel('Average Error')
    plt.xlabel('Stepsize')
    plt.yticks()
    plt.legend()
    plt.savefig('Exc7Task2b.png')











if __name__ == "__main__":
    main()
