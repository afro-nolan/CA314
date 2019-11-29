
class Board:

	def __init__(self, squares):
		"""Initialises the board"""
		self.dimensions = (11,11) #The dimensions of the board
		self.num_squares = 40 #Number of squares on the board
		self.squares = squares #A list of squares on the board