#!bin/usr/python3
import numpy as np
import matplotlib.pyplot as plt

def explicit_euler(f_1,f_2,intervall_start,intervall_end,stepsize):
    '''Explicit euler approximation for two ODEs'''
    x_y_t = [20,20]
    approximations = [x_y_t]
    for step in np.arange(intervall_start+stepsize,intervall_end+stepsize,stepsize):
        x_delta_t = x_y_t[0] + stepsize*f_1(x_y_t[0],x_y_t[1])
        y_delta_t = x_y_t[1] + stepsize*f_2(x_y_t[0],x_y_t[1])

        x_y_t = [x_delta_t,y_delta_t]
        approximations.append(x_y_t)
    return approximations

def runge_kutta(f_1,f_2,intervall_start,intervall_end,stepsize):
    '''Runge Kutta approximation for two ODEs'''
    x_y_t = [20,20]
    approximations = [x_y_t]
    for step in np.arange(intervall_start+stepsize,intervall_end+stepsize,stepsize):
        #approximate x
        k_1 = stepsize*f_1(x_y_t[0],x_y_t[1])
        k_2 = stepsize*f_1(x_y_t[0]+k_1/2,x_y_t[1]+stepsize/2)
        k_3 = stepsize*f_1(x_y_t[0]+k_1/2,x_y_t[1]+stepsize/2)
        k_4 = stepsize*f_1(x_y_t[0]+k_3,x_y_t[1]+stepsize)
        x_delta_t = x_y_t[0]+k_1/6+k_2/3+k_3/3+k_4/6
        #approximate y
        k_1 = stepsize*f_2(x_y_t[0],x_y_t[1])
        k_2 = stepsize*f_2(x_y_t[0]+stepsize/2,x_y_t[1]+k_1/2)
        k_3 = stepsize*f_2(x_y_t[0]+stepsize/2,x_y_t[1]+k_1/2)
        k_4 = stepsize*f_2(x_y_t[0]+stepsize,x_y_t[1]+k_3)
        y_delta_t = x_y_t[1]+k_1/6+k_2/3+k_3/3+k_4/6

        x_y_t = [x_delta_t,y_delta_t]
        approximations.append(x_y_t)
    return approximations



def f_1(x,y):
    return x*(0.3-y*(0.01+0.01))

def f_2(x,y):
    return x*(y*0.01-0.3)

def main():
    t_final = 50

    #subtask a: phase spase diagram
    X = np.arange(0,80,3)
    Y = np.arange(0,40,3)
    XX,YY = np.meshgrid(X,Y)
    U = XX*(0.3 -YY*(0.01 + 0.01))
    V = YY*(XX*0.01 - 0.3)

    plt.figure()
    plt.quiver(XX,YY,U,V)
    plt.ylim((0, 45))
    plt.xlim((0,80))
    plt.ylabel('x_2')
    plt.xlabel('x_1')

    #subtask b: explicit euler approximation
    stepsizes = [0.5,0.1,0.01]
    intervall_start = 0
    intervall_end = t_final
    #explicit euler approximations
    for stepsize in stepsizes:
        approx = explicit_euler(f_1,f_2,intervall_start,intervall_end,stepsize)
        plt.plot([a[0] for a in approx],[a[1] for a in approx],label=f'Explicit Euler stepsize = {stepsize}')

    #subtask c: runge kutta approximation
    approx = runge_kutta(f_1,f_2,intervall_start,intervall_end,0.5)
    plt.plot([a[0] for a in approx],[a[1] for a in approx],label=f'Runge kutta stepsize = 0.5')
    plt.legend()
    plt.savefig('Exc8Task2.png')












if __name__ == "__main__":
    main()
