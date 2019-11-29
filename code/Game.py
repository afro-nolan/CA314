from Board import Board
from Card import Card
from GameCard import GameCard
from Help import Help
from Bank import Bank
from Square import Square

class Game:
	"""Class Game manages the running of the game"""

	def __init__(self):
		"""Initialise all variables for game"""
		self.running = True
		self.players = []
		self.winner = None
		self.board = None
		self.chance = None #Holds chance cards
		self.community_chest = None #Holds community chest cards
		self.help = None
		self.turn = self.find_first_player() #The player's turn

	def add_player(self, player):
		"""Add a player to a game"""
		self.players.append(player)

	def start_game(self):
		"""start the game and enable the window"""
		self.get_player_turn()
		#Initialise the bank and allocate money to each player
		self.initialise_bank()
		#Initialise the board
		self.initialise_board()

	def get_players(self):
		"""Return the players in the game"""
		return self.players

	def initialise_board(self):
		"""Initialise the board"""
		s1 = Square("Go", 0)
		s2 = Square("Crumlin", 1)
		s3 = Square("Community Chest", 2)
		s4 = Square("Kimmage", 3)
		s5 = Square("Income Tax", 4)
		s6 = Square("Busaras Dublin", 5)
		s7 = Square("Rathgar Road", 6)
		s8 = Square("Chance", 7)
		s9 = Square("South Circular Road", 8)
		s10 = Square("Rathmines Road", 9)
		s11 = Square("Jail", 10)
		s12 = Square("Dawson Street", 11)
		s13 = Square("Electric Company", 12)
		s14 = Square("Kildare Street", 13)
		s15 = Square("Nassau Street", 14)
		s16 = Square("Dublin Airport", 15)
		s17 = Square("Pearse Street", 16)
		s18 = Square("Community Chest", 17)
		s19 = Square("Dame Street", 18)
		s20 = Square("Westmoreland Street", 19)
		s21 = Square("Free Parking", 20)
		s22 = Square("Abbey Street", 21)
		s23 = Square("Chance", 22)
		s24 = Square("Capel Street", 23)
		s25 = Square("Henry Street", 24)
		s26 = Square("Heuston Station", 25)
		s27 = Square("Talbot Street", 26)
		s28 = Square("North Earl Street", 27)
		s29 = Square("Waterworks", 28)
		s30 = Square("O'Connell Street", 29)
		s31 = Square("Go To Jail", 30)
		s32 = Square("George's Street", 31)
		s33 = Square("Wicklow Street", 32)
		s34 = Square("Community Chest", 33)
		s35 = Square("Grafton Street", 34)
		s36 = Square("Shannon Airport", 35)
		s37 = Square("Chance", 36)
		s38 = Square("Ailesbury Road", 37)
		s39 = Square("Super Tax", 38)
		s40 = Square("Shrewsbury Road", 39)
		squares = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40]
		for player in self.players:
			player.set_square(s1)
		self.board = Board(squares)

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
		#Allocate money to each player
		self.bank.allocate_money(self.players)

	def find_first_player(self):
		"""Find player to make first move"""
		if len(self.players) < 1:
			return None
		else:
			return self.players[0]

	def get_winner(self):
		"""Get the winner"""
		return self.winner

	def quit_game(self):
		"""quit the game"""
		self.running = False

	def eliminate_player(self, player):
		"""Remove player from game"""
		self.players.remove(player)
		player.stop_playing()

	def get_player_turn(self):
		"""Get the players turn and returns the player"""
		#First move
		if self.turn is None:
			self.turn = self.find_first_player()
			return self.turn
		#Not the first move
		else:
			#get index of current player
			i = 0 
			while i < len(self.players):
				#If we have found it
				if self.players[i] == self.turn:
					break
				i += 1
			#If we are not in the last position, then it is the next person in the lists turn
			if self.players[i] != self.players[-1]:
				self.turn = self.players[i+1]
			#If we are at the end of the list, we need to go back to the start
			else:
				self.turn = self.players[0]
		return self.turn

	def get_turn(self):
		"""Get the current players turn"""
		return self.get_turn



if __name__ == "__main__":
	g = Game()
	g.add_player("a")
	g.add_player("b")
	g.add_player("c")
	print(g.find_first_player())
	print(g.turn)
	print(g.get_player_turn())
	print(g.get_player_turn())






