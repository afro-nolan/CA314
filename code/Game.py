from Board import Board
from Card import Card
from Bank import Bank
from GameCard import GameCard
from Help import Help

class Game:
	"""Class Game manages the running of the game"""

	def __init__(self):
		"""Initialise all variables for game"""
		self.running = True
		self.players = []
		self.winner = None
		self.board = None
		self.cards = []
		self.help = None

	def add_player(self, player):
		"""Add a player to a game"""
		self.players.append(player)

	def start_game(self):
		"""start the game and enable the window"""
		while self.running is True:
			self.find_first_player()

	def get_players(self):
		"""Return the players in the game"""
		return self.players

	def initialise_help(self):
		"""Initialises help menu"""
		self.help = Help("rule.txt")


	def initialise_board(self):
		"""Initialise the board"""
		self.board = Board()

	def initialise_cards(self):
		"""Initialise the cards"""
		gc1 = GameCard("Chance", "It's your birthday! Collect €10 from each player", False, "Chance", 10, self.players, 0)
		self.cards.append(gc1)
		

	def initialise_bank(self):
		"""Initialise bank"""
		self.bank = Bank()

	def find_first_player(self):
		"""Find player to make first move"""
		highest = 0
		first = None
		for player in self.players:
			roll = player.die.roll()
			if roll > highest:
				highest = roll
				first = player
		return first

	def get_winner(self):
		"""Get the winner"""
		return self.winner

	def quit_game(self):
		"""quit the game"""
		self.running = False

	def get_help():
		"""Get help"""
		self.help.show_rules()

	def eliminate_player(self, player):
		"""Remove player from game"""
		self.players.remove(player)
		player.stop_playing()







