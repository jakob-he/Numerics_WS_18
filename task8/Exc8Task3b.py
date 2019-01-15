#!bin/usr/python3
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(f,intervall_start,intervall_end,stepsize):
    x_t = 0
    approximations = [x_t]
    for step in np.arange(intervall_start+stepsize,intervall_end+stepsize,stepsize):
        #approximate x
        k_1 = stepsize*f(step,x_t)
        k_2 = stepsize*f(step+stepsize/2,x_t+k_1/2)
        k_3 = stepsize*f(step+stepsize/2,x_t+k_1/2)
        k_4 = stepsize*f(step+stepsize,x_t+k_3)
        x_delta_t = x_t+k_1/6+k_2/3+k_3/3+k_4/6
        x_t = x_delta_t
        approximations.append(x_delta_t)
    return approximations


def f(t,x_t):
    return 0.5*(200*np.exp(-0.5*t))-0.3*x_t

def main():
    stepsizes = [0.1,0.25,0.5]
    means = []
    intervall_start = 0
    intervall_end = 24
    for stepsize in stepsizes:
        approximations = runge_kutta(f,intervall_start,intervall_end,stepsize)
        ts = np.arange(intervall_start,intervall_end+stepsize,stepsize)
        real_xs = [(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t))) for t in ts]
        means.append(np.mean(abs(np.subtract(real_xs,approximations))))

    plt.loglog(stepsizes,stepsizes,color='red', label=r'$\Delta$ t')
    plt.loglog(stepsizes,means,linestyle=':',marker='o', label = 'Runge Kutta')
    plt.title('Average Error: Runge Kutta')
    plt.ylabel('Average Error')
    plt.xlabel('Stepsize')
    plt.yticks()
    plt.legend()
    plt.savefig('Exc8Task3b.png')











if __name__ == "__main__":
    main()
