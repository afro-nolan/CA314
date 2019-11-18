from Game import Game
from Square import Square
import random

class CardSquare(Square):
	"""A card square on the board"""

	def __init__(self, name, location):
		"""Initialise the card square"""
		super().__init__(name, location)
		
	def get_card(self):
		"""Get a card from the deck"""
		index = random.randint(0,109)
		card = Game.cards[index]
		card.show_card()