#Simple MCMC Templete

import numpy as np
import pdb
import pylab as pl
import matplotlib.pyplot as plt
from scipy.stats import norm


# target distribution
def pi(x):
	return 0.3*norm(30,10).pdf(x)+0.7*norm(30,10).pdf(x)




S = [5,20,40]
Total_points = 2000

for s in S:
	# acceptance and trial counter
	Accepted_counter = 0
	Tried = 0
	X = [10]
	Q = [0]
	while Accepted_counter < Total_points:

		r = np.random.rand()
		x_new = np.random.normal(X[-1],s)
		Q_new = norm(x_new,s).pdf(X[-1])/norm(X[-1],s).pdf(x_new)
		Tried += 1

		if r < min(1,Q_new*(pi(x_new)/pi(X[-1]))):

			# if acepted.
			X.append(x_new)
			Q.append(Q_new)

			Accepted_counter += 1

			#print x_new
			#print ("Acceptance Rate %f"%(Accepted_counter/float(Tried)))

	# The list X has all your samples.

	###
	#  Plot to see the autocorrelation of your data set.
	###
	pl.figure(1)
	pl.acorr(X-np.average(X),maxlags=400,usevlines=True,linestyle='-')
	pl.axhline(y=0.05,linestyle="dashed")
	pl.title(f"Autocorrelation for S={s}")
	pl.savefig(f"Figure_S_{s}.png")
