from Bank import Bank

class Card:

	def __init__(self, name, description, keep):
		"""Initialises the card"""
		self.name = name
		self.description = description
		self.keep = keep

	def show_card(self):
		"""Shows the card"""
		return self.name + " " + self.description

	def put_back(self):
		"""Put the card back in the deck"""
		Bank.place_card(self)

	def take_card(self, player):
		"""Take a card and put in inventory"""
		if self.keep is True:
			Bank.cards.remove(self)
			self.player.inventory.place_card(self)
		else:
			return False