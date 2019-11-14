import random

class Die:

	def __init__(self):
		self.sides = [1,2,3,4,5,6]

	def roll(self):
		"""Roll the dice and return the sum of the 2 die"""
		index = random.randint(0,5)
		index2 = random.randint(0,5)
		return self.sides[index] + self.sides[index2]