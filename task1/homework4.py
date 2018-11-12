'''
Short script for saving a stochiometric matrix and computing ODEs for specific x and k values.
Without any input both the matrix and ODEs are saved. If only one is needed, a command line
argument can be used as defined in parse_arguments().
'''


import argparse
import numpy as np


def parse_arguments():
    '''Parses command line arguments'''
    parser = argparse.ArgumentParser(description = 'Create a stochiometric matrix and compute ODEs')
    parser.add_argument('--a', action = 'store_true', help = 'subtask a: Save stochiometric matrix in txt file')
    parser.add_argument('--b', action = 'store_true', help = 'subtask b: Compute ODEs')
    args = parser.parse_args()
    return args




def save_sto_matrix():
    '''Saves stochiometric matrix to txt file'''
    #fill matrix with known values
    sto_matrix = np.matrix('1 -1 -1 0 1; 0 0 1 -1 -1; 0 0 0 0 1; 0 0 -1 0 0')
    #save matrix
    with open('SMatrix.txt' ,'wb') as output:
        np.savetxt(output,sto_matrix,delimiter = ",",fmt = '%d')


def compute_odes():
    #set x values
    x_1 = 5
    x_2 = 25
    x_3 = 15
    x_4 = 5

    #set k values
    k_1 = 5
    k_2 = 3
    k_3 = 12
    k_4 = 7
    k_5 = 3

    #calculate reaction rates
    r_1 = k_1
    r_2 = k_2 * x_1
    r_3 = k_3 * x_1 * x_4
    r_4 = k_4 * x_2
    r_5 = k_5 * x_2

    #calculate ODEs at time step 1 assuming V_i for all i = 1
    dt_x_1 = r_1 - r_2 - r_3 + r_5
    dt_x_2 = r_3 - r_4 -r_5
    dt_x_3 = r_5
    dt_x_4 = -r_3

    result_mat = np.matrix(f'{dt_x_1}; {dt_x_2}; {dt_x_3}; {dt_x_4}')

    #save results
    with open('ODEValue.txt' ,'wb') as output:
        np.savetxt(output,result_mat,fmt='%d')






def main():
    '''The main function executes either both subtask a and b if no input is given or the user specified subtask(s)'''
    args = parse_arguments()
    if not args.a and not args.b:
        save_sto_matrix()
        compute_odes()
    if args.a:
        save_sto_matrix()
    elif args.b:
        compute_odes()
















if __name__ == "__main__":
    main()
