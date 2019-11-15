from Square import Square

class Go(Square):

	def __init__(self, location):
		"""Initialise Go Square"""
		super().__init__(location)

	def collect_money(self, player):
		player.inventory.deposit(200)

