####
# Trajectories for the SIR model in Exercise 3
# Author The big V.
####

import numpy as np
import matplotlib.pyplot as pl

#######################################################################################
#  Initialising the Model
#######################################################################################
'''
Stochiomtry
'''

Stoc = np.array(	[[1,-1,-1,0,0,0],
					[0,0,1,-1,-1,0],
					[0,0,0,0,1,-1] ,
					[0,0,0,1,0,0]]
				)

'''
Propensities
'''

lam 	= 1e-4
delta 	= 1e-8
beta 	= 5e-5
k_r		= 0.3

def Props(X):
	return np.array([lam,X[0]*delta,X[0]*X[1]*beta,delta*X[1]*3e7,X[1]*k_r,X[2]*delta])

'''
Initial Start
'''

X_0 = np.array([lam/delta,5,0,0])


#######################################################################################
#Part B    Plots the trajectories for N = 3 simulations up to time T = 10.
#######################################################################################

from SSA import SSA

for i in range(3):

	# get a single realisation
	states, times = SSA(Stoc,Props,X_0,10)

	# plot each specie into a different figure
	for j in range(4):
		pl.figure(j)
		pl.step(times,states[j,:],label="traj %d"%(i+1))
		pl.legend()

# Add labels and axes
for i in range(4):
	pl.figure(i)
	pl.title("Species x_%d"%(i+1))
	pl.xlabel("Time")
	pl.ylabel("Species Count x_%d"%(i+1))

pl.show()

#######################################################################################
#Part C D  	Perform N = 1000 simulations, generate a histogram of the number of x2 
#			at time T = 10 and depict the probability that 0,. . . , 20 individuals 
#			are infected by T = 10. What is the probability that the infection is 
#			still ongoing at T = 10?
#######################################################################################

X_10 = np.zeros((4,1000))

for i in range(1000):
	# get a single realisation
	states, times = SSA(Stoc,Props,X_0,10)
	X_10[:,i] = states[:,-1] # we only need the last state.

# Histogram Part C
pl.hist(X_10[1,:],bins=range(21),normed=True)
pl.xlabel("Population of X_2")
pl.ylabel(" Probability of Observing X_2 at time T=10 ")
pl.show()


# Histogram Part D
pl.hist(X_10[3,:],bins=range(36),normed=True)
pl.xlabel("Population of X_4")
pl.ylabel(" Probability of Observing X_4 at time T=10 ")
pl.show()



