from Square import Square
import random

class CardSquare(Square):
	"""A card square on the board"""

	def __init__(self, name, location):
		"""Initialise the card square"""
		super().__init__(name, location)
		
	def get_card(self):
		"""Get a card from the deck"""
		#TODO: Get card decks!!
		if self.get_name() == "Chance":
			card = random.choice(list(chance_deck))
		else:
			card = random.choice(list(community_deck))

	def get_name(self):
		"""Return name of the card square"""
		return self.name