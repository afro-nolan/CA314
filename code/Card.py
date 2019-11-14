from Bank import Bank

class Card:

	def __init__(self, name, description, keep):
		"""Initialises the card"""
		self.name = name
		self.description = description
		self.keep = keep

	def show_card(self):
		return self.name + " " + self.description

	def put_back(self):
		Bank.place_card(self)

	def take_card(self, player):
		if self.keep is True:
			self.player.inventory.place_card(self)
		else:
			return False