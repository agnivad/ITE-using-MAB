import numpy as np
from .sine_base import Sine_Base


class Simulation:
	"""
	Synthetic environment for simulation
	"""
	def __init__(self, C=np.array([0, 1]), D=2, base_functions=np.array([Sine_Base(), Sine_Base()]), drift_rate=0, drift_over_time=1000, sudden_drift=False, drift_moments=np.array([]), std=0):
		self.C = C
		self.base_functions = base_functions
		self.D = D
		self.dim_count = D

		self.drift_rate = drift_rate
		self.drift_over_time = drift_over_time
		self.drift_moments = drift_moments
		self.sudden_drift = sudden_drift
		self.current_drift = 0
		self.drift = 0

		self.std = std

		self.current_state = np.empty(0)
		self.time = 0
	
	def get_new_state(self):
		"""
		Initialize current state as random
		:return x: state
		"""
		x = np.random.random_sample(self.D)
		self.current_state = x
		return x

	def reset(self):
		"""
		Reset time, current_drift and drift
		"""
		self.time = 0
		self.current_drift = 0
		self.drift = 0
	
	def choose_cause(self, C, drift=True, n=True):
		"""
		Create data from the synthetic probability distribution
		:param int C: Treatment
		:param bool drift: to decide whether to apply drift or not
		:param bool n: to decide whether to apply noise or not
		:return tuple: new state, response to Treatment
		"""
		x = self.current_state

		self.time += 1
		self.update_drift()
		
		p = self.get_response_rate(C, x, drift)
		if n:						
			p = self.apply_noise(p)

		return self.get_new_state(), np.random.binomial(1, p)
	
	def apply_noise(self, p):
		"""
		Helper function to add noise

		:param float p:
		:return: float p: noise value
		"""
		if self.std:
			return (1 + np.exp(-3 * np.random.normal(p, self.std))) ** -1
		return p

	def get_response_rate(self, C, x, drift=True):
		"""
		Compute the probability distribution of Y|C,x with base_function

		:param int C: Treatment
		:param np.array x: Context
		:param bool drift: drift
		:return float: Probability value
		"""
		d = 0
		if drift:
			if self.drift:
				d = self.drift
		return self.base_functions[C].eval(x, d, C)

	def update_drift(self):
		"""
		Helper function to update drift
		"""
		drift = 0
		if self.sudden_drift:
			if len(self.drift_moments) == 0:
				drift = self.drift_rate * np.random.binomial(1, 1 / self.drift_over_time)
			elif np.any(self.drift_moments == self.time):
				drift = self.drift_rate
		else:
			drift = self.drift_rate / self.drift_over_time

		self.drift += drift
		self.current_drift = drift
	
	def get_sim_uplift(self, x):
		"""
		Compute the uplift with drift

		:param np.array x: Context
		:return float: uplift value
		"""
		return self.get_response_rate(1, x, drift=True) - self.get_response_rate(0, x, drift=True)