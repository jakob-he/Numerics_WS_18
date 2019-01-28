# /bin/usr/python3
import numpy as np
import argparse
import math
import matplotlib.pyplot as plt


@np.vectorize
def x(t, k_a, k_e):
    return 200 * (k_a / (k_a - k_e)) * (np.exp(-k_e * t) - np.exp(-k_a * t))


@np.vectorize
def y(t, k_a, k_e):
    return x(t, k_a, k_e)


@np.vectorize
def likeli(t_i, y_i, sigma_i, k_a, k_e):
    return (np.exp(-(y_i - x(t_i, k_a, k_e))) / (2 * sigma_i**2)) / np.sqrt(2 * sigma_i**2 * np.pi)


@np.vectorize
def ols(t, y, k_a, k_e):
    return (y - x(t, k_a, k_e))**2


@np.vectorize
def wls(t, y, sigma, k_a, k_e):
    return ((y - x(t, k_a, k_e)) / sigma)**2


def main():
    # subtask a
    # read Input
    with open("Input.txt", "r") as input:
        k_a, k_e = [float(line) for line in input]

    # set measurements and time
    Y = [48.52, 70.61, 82.57, 72.87, 35.09, 7.37]
    T = [1, 2, 5, 7, 12, 24]
    S = [4, 4, 16, 4, 1, 4]

    # compute likelihood given the formula given in exercise 11
    likelihood = np.prod(likeli(T, Y, S, k_a, k_e))
    neg_log_likelihood = -np.log(likelihood)

    # compute the sum of ordinary least squares
    ord_least_squares = np.sum(ols(T, Y, k_a, k_e))

    # compute the sum of weighted least squares
    weigh_least_sqaures = np.sum(wls(T, Y, S, k_a, k_e))

    # save all three numbers to a text file
    with open("Exc11Task1.txt", "w") as output:
        for number in [neg_log_likelihood, ord_least_squares, weigh_least_sqaures]:
            output.write(f"{number}\n")

    # subtask b
    # creating meshgrid
    k_as = np.linspace(0.1, 0.4, 30)
    k_es = np.linspace(0.15, 0.35, 30)
    k_as, k_es = np.meshgrid(k_as, k_es)

    # negative log likelihood
    likelihoods = -np.log(np.prod([likeli(T[i], Y[i], S[i], k_as, k_es)
                                   for i in range(len(Y))], axis=0, dtype=np.longfloat))

    plt.figure(1)
    plt.contour(k_as, k_es, likelihoods)
    plt.title("Likelihood")
    plt.savefig("Exc11Task1b_li.png")

    # ordinary least squares
    ord_least_squares = np.sum([ols(T[i], Y[i], k_as, k_es)
                                for i in range(len(Y))], axis=0)

    plt.figure(2)
    plt.contour(k_as, k_es, ord_least_squares)
    plt.title("Ordinary least squares")
    plt.savefig("Exc11Task1b_ols.png")

    # weighted least squares
    weigh_least_squares = np.sum(
        [wls(T[i], Y[i], S[i], k_as, k_es) for i in range(len(Y))], axis=0)

    plt.figure(3)
    plt.contour(k_as, k_es, weigh_least_squares)
    plt.title("Weighted least squares")
    plt.savefig("Exc11Task1b_wls.png")

if __name__ == "__main__":
    main()
