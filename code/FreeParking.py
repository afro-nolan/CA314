
from Square import Square

class FreeParking(Square):


	def __init__(self):
		"""Initialise free parking space"""
		super().__init__(name, location)

	def get_location(self):
		"""Get the location of the free parking square"""
		return self.location