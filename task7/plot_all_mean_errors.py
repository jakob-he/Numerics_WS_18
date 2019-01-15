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

def explicit_midpoint(func,intervall_start,intervall_end,stepsize):
    x_t = 0
    approximations = [x_t]
    for step in np.arange(intervall_start+stepsize,intervall_end+stepsize,stepsize):
        x_delta_t = x_t + stepsize*func(step+(stepsize/2),x_t+(stepsize/2)*func(step,x_t))
        x_t = x_delta_t
        approximations.append(x_delta_t)
    return approximations

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


def main():
    stepsizes = [0.1,0.25,0.5]
    exp_euler_means = []
    imp_euler_means = []
    exp_midpoint_means = []
    intervall_start = 0
    intervall_end = 24
    for stepsize in stepsizes:
        approximations = explicit_euler(f,intervall_start,intervall_end,stepsize)
        ts = np.arange(intervall_start,intervall_end+stepsize,stepsize)
        real_xs = [(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t))) for t in ts]
        exp_euler_means.append(np.mean(abs(np.subtract(real_xs,approximations))))
        approximations = implicit_euler(f,intervall_start,intervall_end,stepsize)
        ts = np.arange(intervall_start,intervall_end+stepsize,stepsize)
        real_xs = [(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t))) for t in ts]
        imp_euler_means.append(np.mean(abs(np.subtract(real_xs,approximations))))
        approximations = explicit_midpoint(f,intervall_start,intervall_end,stepsize)
        ts = np.arange(intervall_start,intervall_end+stepsize,stepsize)
        real_xs = [(200*(0.5/(0.5-0.3))*(np.exp(-0.3*t)-np.exp(-0.5*t))) for t in ts]
        exp_midpoint_means.append(np.mean(abs(np.subtract(real_xs,approximations))))

    plt.loglog(stepsizes,stepsizes,color='red', label=r'$\Delta$ t')
    plt.loglog(stepsizes,exp_euler_means,linestyle=':',marker='o', label = 'Explicit Euler')
    plt.loglog(stepsizes,imp_euler_means,linestyle=':',marker='o', label = 'Implicit Euler')
    plt.loglog(stepsizes,exp_midpoint_means,linestyle=':',marker='o', label = 'Explicit Midpoint')
    plt.title('Average Errors')
    plt.ylabel('Average Error')
    plt.xlabel('Stepsize')
    plt.yticks()
    plt.legend()
    plt.savefig('all_mean_errors.png')











if __name__ == "__main__":
    main()
