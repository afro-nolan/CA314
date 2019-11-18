
class Auction:
	"""Auction class"""

	def __init__(self, players, property, building initial_bid):
		"""Initialise auction"""
		self.players = players
		self.property = property
		self.building = building
		self.initial_bid = initial_bid
		self.current_bid = initial_bid

	def get_bid(self):
		"""get players bid"""
		return self.current_bid

	def get_players(self):
		"""get players in bid"""
		return self.players

	def get_property(self):
		"""get property being bidded on"""
		return self.property

	def get_initial_bid(self):
		"""Get intiial bid"""
		return self.initial_bid

	def get_current_bid(self):
		"""Get current bid"""
		return self.current_bid

	def get_building(self):
		"""Get building being bidded on"""
		return self.building