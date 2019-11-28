from Game import Game
from Square import Square
import random

class CardSquare(Square):
	"""A card square on the board"""

	def __init__(self, name, location, chance_deck, community_deck):
		"""Initialise the card square"""
		super().__init__(name, location)
		self.chance_deck = chance_deck
		self.community_deck = community_deck
		
	def get_card(self):
		"""Get a card from the deck"""
		if self.get_name() == "Chance":
			card = random.choice(list(chance_deck))
		else:
			card = random.choice(list(community_deck))

	def get_name(self):
		"""Return name of the card square"""
		return self.name