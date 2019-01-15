#Simple MCMC Templete

import numpy as np 
import pdb
import pylab as pl
import matplotlib.pyplot as plt
#from scipy.stats import norm


# target distribution 
def pi(params):
	#calculations
	return  


# acceptance and trial counter
Accepted_counter = 0
Tried = 0

# Total number of steps to take in a walk 

S =  										# scaling parameter
X = ["Starting State"]  					# starting state
Q = ["probability of the starting states"] 



while Accepted_counter < Total_points:

	r = np.random.rand()
	rho = # transition probability ratio
	x_new = # state update

	Q_new = pi("probability of the new states")
	Tried += 1

	if ("ACCEPTANCE CRITERION HERE"):

		# if acepted.
		X.append(x_new)
		Q.append(Q_new)

		Accepted_counter += 1

		#print x_new
		print "Acceptance Rate %f"%(Accepted_counter/float(Tried))

# The list X has all your samples. 


###
#  Plot to see the autocorrelation of your data set. 
###
pl.figure(1)
pl.acorr(X-np.average(X),maxlags=400,usevlines=True,linestyle='-',marker=None)
pl.axhline(y=0.05,linestyle="dashed")
