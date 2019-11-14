from Game import Game
from Square import Square
import random

class CardSquare(Square):

	def __init__(self, name, location):
		super().__init__(name, location)
		
	def get_card(self):
		index = random.randint(0,109)
		card = Game.cards[index]
		card.show_card()