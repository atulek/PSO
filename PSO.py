import numpy as np
from TestFunc import TestFunc

class PSO:
	def __init__(self, test_func, repeat=5, maxit=100, npop=50, nvar=50, c1=1.4962, c2=1.4962, w=0.7298, wdamp=1.0):
	
		self.costfunc = test_func.costfunc
		self.nvar = nvar
		self.varmin = test_func.varmin
		self.varmax = test_func.varmax
		
		self.maxit = maxit
		self.npop = npop
		self.c1 = c1
		self.c2 = c2
		self.w = w
		self.wdamp = wdamp

	def run(self):

		# Empty Particle Template
		empty_particle = {
			'position': None,
			'velocity': None,
			'cost': None,
			'best_position': None,
			'best_cost': None,
		}

		# Extract Problem Info
		# CostFunction = problem['CostFunction']
		# VarMin = problem['VarMin']
		# VarMax = problem['VarMax']
		# nVar = problem['nVar']

		# Initialize Global Best
		gbest = {'position': None, 'cost': np.inf}

		# Create Initial Population
		pop = []
		for i in range(0, self.npop):
			pop.append(empty_particle.copy())
			pop[i]['position'] = np.random.uniform(self.varmin, self.varmax, self.nvar)
			pop[i]['velocity'] = np.zeros(self.nvar)
			pop[i]['cost'] = self.costfunc(pop[i]['position'])
			pop[i]['best_position'] = pop[i]['position'].copy()
			pop[i]['best_cost'] = pop[i]['cost']

			if pop[i]['best_cost'] < gbest['cost']:
				gbest['position'] = pop[i]['best_position'].copy()
				gbest['cost'] = pop[i]['best_cost']

		bestcost = np.empty(self.maxit)

		# PSO Loop
		for it in range(0, self.maxit):
			for i in range(0, self.npop):

				pop[i]['velocity'] = self.w * pop[i]['velocity'] \
									 + self.c1 * np.random.rand(self.nvar) * (pop[i]['best_position'] - pop[i]['position']) \
									 + self.c2 * np.random.rand(self.nvar) * (gbest['position'] - pop[i]['position'])

				pop[i]['position'] += pop[i]['velocity']
				pop[i]['position'] = np.maximum(pop[i]['position'], self.varmin)
				pop[i]['position'] = np.minimum(pop[i]['position'], self.varmax)

				pop[i]['cost'] = self.costfunc(pop[i]['position'])

				if pop[i]['cost'] < pop[i]['best_cost']:
					pop[i]['best_position'] = pop[i]['position'].copy()
					pop[i]['best_cost'] = pop[i]['cost']

					if pop[i]['best_cost'] < gbest['cost']:
						gbest['position'] = pop[i]['best_position'].copy()
						gbest['cost'] = pop[i]['best_cost']

			self.w *= self.wdamp
			print('Iteration {}: Best Cost = {}'.format(it, gbest['cost']))
			bestcost[it] = gbest["cost"]

		print(bestcost)
		return bestcost

# Start Time for tic and tov functions
# startTime_for_tictoc = 0
#
# # Start measuring time elapsed
# def tic():
# 	import time
# 	global startTime_for_tictoc
# 	startTime_for_tictoc = time.time()
#
# # End mesuring time elapsed
# def toc():
# 	import time, math
# 	if 'startTime_for_tictoc' in globals():
# 		dt = math.floor(100*(time.time() - startTime_for_tictoc))/100.
# 		print('Elapsed time is {} second(s).'.format(dt))
# 	else:
# 		print('Start time not set. You should call tic before toc.')
