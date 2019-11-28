from Board import Board
from Card import Card
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
		self.chance = None #Holds chance cards
		self.community_chest = None
		self.help = None
		self.turn = None

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
		self.chance = {
			GameCard("Chance Card", "Take a trip to King's Cross Station. If you pass Go collect 200.", False, "Move", None, None, "King's Cross Station" ) : "resources/chance1.jpg",
			GameCard("Chance Card", "You have been elected Chairman of the Board. Pay each player 50.", False, "Lose", 50, self.players, None) : "resources/chance3.jpg",
			GameCard("Chance Card", "Advance to the nearest utility. If unowned you may buy it from the bank. If owned, throw dice and pay owner a total ten times thrown.", False, "Move", None, None, "Utility") : "resources/chance4.jpg",
			GameCard("Chance Card", "Go back three spaces.", False, "Move", None, None, -3 ) : "resources/chance5.jpg",
			GameCard("Chance Card", "Your building loan matures. Collect 150.", False, "Gain", 150, None, None ) : "resources/chance6.jpg",
			GameCard("Chance Card", "Advance to Pall Mall. If you pass go collect 200.", False, "Move", None, None, "Pall Mall") : "resources/chance7.jpg",
			GameCard("Chance Card", "Make general repairs on all your property: For each house pay 25, for each hotel pay 100.", False, "Lose", (25, 100), None, None) :"resources/chance8.jpg",
			GameCard("Chance Card","Go to Jail. Go directly to jail, Do not pass Go, Do not collect 200.", False, "Jail", None, None, "Jail") : "resources/chance9.jpg",
			GameCard("Chance Card", "Get out of jail Free. This card may be kept until needed or traded", True, "GetOutOfJail", None, None, None) : "resources/chance12.jpg",
		}
		

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
		self.turn = first

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







