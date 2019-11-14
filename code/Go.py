from Square import Square

class Go(Square):

	def __init__(self, location):
		"""Initialise Go Square"""
		self.location = location

	def collect_money(self, player):
		player.inventory.deposit(200)

