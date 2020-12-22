import numpy as np
import math


class Sine_Base:
	"""
	Create Sine Base for the synthetic simulation (case 2 treatment)
	"""
	def __init__(self, D=2, f=1, G=np.full(2, .5)):
		self.D = D
		self.f = f
		
		if len(G) != D:
			raise ValueError("Displacement vector G does not match dimension count D!")

		self.G = G
	
	def eval(self, x, d, C):
		"""
		Formulate the sine base

		:param np.array x: context
		:param float d: drift
		:param int C: Treatment
		:return float:
		"""
		interaction = 1

		for i in range(self.D):
			interaction *= (x[i] + abs(C - 1) * self.G[i])

		return (math.sin((self.f) * interaction + d) + 1) / 2
