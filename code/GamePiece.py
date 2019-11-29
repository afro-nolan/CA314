

class GamePiece:
	"""Represents a game piece"""

	def __init__(self, name, xpos=0):
		"""Initialises game piece"""
		self.name = name
		self.xpos = xpos #x position on screen
		#self.ypos = ypos #y position on screen
		self.sprite = "" #sprite image

	def update_positions(self, x):
		"""Update position on screen"""
		self.xpos = x

	def get_name(self):
		return self.name

	def get_position(self):
		#return (self.xpos, self.ypos)
		return self.xpos

	
