
class Square:

	def __init__(self, name, location):
		"""Initialises the square"""
		self.name = name #Is a string that is the name of the square
		self.location = location #Is a tuple that represents the location on the board

	def get_type(self):
		"""Returns the type of square"""
		return self.type

	def get_location(self):
		"""Returns the location of square"""
		return self.location

	def get_name(self):
		"""Returns the name of the square"""
		return self.name
