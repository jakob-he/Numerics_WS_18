####
# Code For Constructing Realisations of Kurtz Processes.
# Author The big V.
# This code was changed from the original version, such that every
# time step is 0.1
####

import numpy as np

def Find_Reaction_Index(a):
	"""
	@brief The function takes in the propensity vector and returns the index of a possible reaction candidate.
	@param a : Array (num_reaction,1)

	"""
	# small hack as the numpy uniform random number includes 0
	r = np.random.rand()
	while r == 0:
		r = np.random.rand()

	return np.sum(np.cumsum(a) < r*np.sum(a))

def SSA(Stochiometry,Propensities,X_0,t_final):
	"""
	@brief  The Stochastic Simulation Algorithm. Given the stochiometry, propensities and the initial state; the algorithm
			gives a sample of the Kurtz process at $t_final.$

	@param Stochiometry : Numpy Array (Num_species,Num_reaction).
	@param Propensities : Function which given a state, returns the respective reaction propensities.
	@param X_0			: Numpy Array (Num_species, 1).
	@param t_final		: positive number.

	"""

	t = 0.0
	x = X_0

	X_store = []
	T_store = []

	while t < t_final:

		a = Propensities(x)

		# First Jump Time
		tau = 0.1

		# Test if we have jumped to far
		if (t + tau > t_final) or (np.sum(a) == 0):
			X_store.append(x)
			T_store.append(t_final)
			return np.array(X_store).T,np.array(T_store)
		else:
			# Since we have not, we need to find the next reaction
			t = t + tau
			j = Find_Reaction_Index(a)
			x = x + Stochiometry[:,j]

			# Update Our Storage
			X_store.append(x)
			T_store.append(t)
