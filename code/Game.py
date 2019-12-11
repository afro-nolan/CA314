from Board import Board
from Card import Card
from GameCard import GameCard
from Help import Help
from Bank import Bank
from Square import Square
from Station import Station
from Go import Go
from Property import Property
from UtilitySquare import UtilitySquare
from Tax import Tax
from Jail import Jail
from TitleDeedCard import TitleDeedCard
from CardSquare import CardSquare
from FreeParking import FreeParking
from GoToJail import GoToJail

class Game:
	"""Class Game manages the running of the game"""

	def __init__(self):
		"""Initialise all variables for game"""
		self.running = True
		self.players = []
		self.winner = "Aifric"
		self.board = None
		self.bank = None
		self.chance = None #Holds chance cards
		self.community_chest = None #Holds community chest cards
		self.help = None
		self.turn = self.find_first_player() #The player's turn

	def add_player(self, player):
		"""Add a player to a game"""
		self.players.append(player)

	def get_bank(self):
		return self.bank

	def start_game(self):
		"""start the game and enable the window"""
		self.get_player_turn()
		#Initialise the bank and allocate money to each player
		self.initialise_bank()
		#Initialise the board
		self.initialise_board()
		self.initialise_cards()

	def get_players(self):
		"""Return the players in the game"""
		return self.players

	def initialise_board(self):
		"""Initialise the board"""
		s1 = Go("Go", 0)
		s2 = Property("Crumlin", TitleDeedCard("Crumlin", True, 60, 30,[2,10,30,90,160,250], "A", "brown",50, 50, "resources/crumlin.png"), 1, False, None)
		s3 = CardSquare("Community Chest", 2)
		s4 = Property("Kimmage", TitleDeedCard("Kimmage", True, 60, 30, [4,20,60,180,320,450], "A", "brown", 50, 50, "resources/kimmage.png"), 3, False, None)
		s5 = Tax("Income Tax", 4, 200)
		s6 = Station("Busaras Dublin", False, False, 200, TitleDeedCard("Busaras Dublin", True, 200, 100, [25, 50, 100, 200], "B", None, None, None), 5)
		s7 = Property("Rathgar Road", TitleDeedCard("Rathgar Road", True, 100, 50, [6,30,90,270,400,550], "C", "lightblue", 50, 50, "resources/rathgar.png"), 6, False, None)
		s8 = CardSquare("Chance", 7)
		s9 = Property("South Circular Road", TitleDeedCard("South Circular Road", True, 100, 50, [6,30,90,270,400,550], "C", "lightblue", 50, 50, "resources/southcircular.png"), 8, False, None)
		s10 = Property("Rathmines Road", TitleDeedCard("Rathmines Road", True, 120, 60, [8, 40, 100, 300, 450, 600], "C", "lightblue", 50, 50, "resources/rathmines.png"), 9, False, None)
		s11 = Jail("Jail", 10)
		s12 = Property("Dawson Street", TitleDeedCard("Dawson Street", True, 140, 70, [10, 50, 150, 450, 625, 750], "D", "pink", 100, 100, "resources/dawson.png"), 11, False, None)
		s13 = UtilitySquare("Electric Company", 12, TitleDeedCard("Electric Company", True, 150, 75, [4, 10], "E", None, None, None, "resources/Utility1.png"), 150)
		s14 = Property("Kildare Street", TitleDeedCard("Kildare Street", True, 140, 70, [10, 50, 150, 450, 625, 750], "D", "pink", 100, 100, "resources/kildare.png"), 13, False, None)
		s15 = Property("Nassau Street", TitleDeedCard("Nassau Street", True, 160, 80, [12, 60, 180, 500, 700, 900], "D", "pink", 100, 100, "resources/nassau.png"), 14, False, None)
		s16 = Station("Dublin Airport", False, None, 200, TitleDeedCard("Dublin Airport", True, 200, 100, [25, 50, 100, 200], "B", None, None, None), 15)
		s17 = Property("Pearse Street", TitleDeedCard("Pearse Street", True, 180, 90, [14, 70, 200, 550, 750, 950], "F", "orange", 100, 100, "resources/pearse.png"), 16, False, None)
		s18 = CardSquare("Community Chest", 17)
		s19 = Property("Dame Street",TitleDeedCard("Dame Street", True, 180, 90, [14, 70, 200, 550, 750, 950], "F", "orange", 100, 100, "dame.png"), 18, False, None)
		s20 = Property("Westmoreland Street", TitleDeedCard("Westmoreland Street", True, 200, 100, [16, 80, 220, 600, 800, 1000], "F", "orange", 100, 100, "resources/westmoreland.png"), 19, False, None)
		s21 = FreeParking("Free Parking", 20)
		s22 = Property("Abbey Street", TitleDeedCard("Abbey Street", True, 220, 110, [18, 90, 250, 700, 875, 1050], "G", "red", 150, 150, "resources/abbey.png"), 21, False, None)
		s23 = CardSquare("Chance", 22)
		s24 = Property("Capel Street", TitleDeedCard("Capel Street", True, 220, 110, [18, 90, 250, 700, 875, 1050], "G", "red", 150, 150, "resources/capel.png"), 23, False, None)
		s25 = Property("Henry Street", TitleDeedCard("Henry Street", True, 240, 120, [20, 100, 300, 750, 925, 1100], "G", "red", 150, 150, "resources/henry.png"), 24, False, None)
		s26 = Station("Heuston Station", False, False, 200, TitleDeedCard("Heuston Station", True, 200, 100, [25, 50, 100, 200], "B", None, None, None), 25)
		s27 = Property("Talbot Street", TitleDeedCard("Talbot Street", True, 260, 130, [22, 110, 330, 800, 975, 1150], "H", "yellow", 150, 150, "resources/talbot.png"), 26, False, None)
		s28 = Property("North Earl Street", TitleDeedCard("North Earl Street", True, 260, 130, [22, 110, 330, 800, 975, 1150], "H", "yellow", 150, 150, "resources/northearl.png"), 27, False, None)
		s29 = UtilitySquare("Waterworks", 28, TitleDeedCard("Waterworks", True, 150, 75, [4, 10], "E", None, None, None, "resources/Utility.png"), 150)
		s30 = Property("O'Connell Street", TitleDeedCard("O'Connell Street", True, 280, 140, [24, 120, 360, 850, 1025, 1200], "H", "yellow", 150, 150, "resources/oconnellstreet.png"), 29, False, None)
		s31 = GoToJail("Go To Jail", 30)
		s32 = Property("George's Street", TitleDeedCard("George's Street", True, 300, 150, [26, 130, 390, 900, 1100, 1275], "I", "green", 200, 200, "resources/George.png"), 31, False, None)
		s33 = Property("Wicklow Street", TitleDeedCard("Wicklow Street", True, 300, 150, [26, 130, 390, 900, 1100, 1275], "I", "green", 200, 200, "resources/wicklow.png"), 32, False, None)
		s34 = CardSquare("Community Chest", 33)
		s35 = Property("Grafton Street", TitleDeedCard("Grafton Street", True, 320, 160, [28, 150, 450, 1000, 1200, 1400], "I", "green", 200, 200, "resources/Grafton.png"), 34, False, None)
		s36 = Station("Shannon Airport", False, None, 200, TitleDeedCard("Shannon Airport", True, 200, 100, [25,50,100,200], "B", None, None, None), 35)
		s37 = CardSquare("Chance", 36)
		s38 = Property("Ailesbury Road", TitleDeedCard("Ailesbury Road", True, 350, 175, [35, 175, 500, 1100, 1300, 1500], "J", "navy", 200, 200, "resources/ailesbury.png"), 37, False, None)
		s39 = Tax("Super Tax", 38, 100)
		s40 = Property("Shrewsbury Road", TitleDeedCard("Shrewsbury Road", True, 400, 200, [50, 200, 600, 1400, 1700, 2000], "J", "navy", 200, 200, "resources/shrewsbury.png"), 39, False, None)
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
		#self.bank.allocate_money(self.players)

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
		return self.turn



if __name__ == "__main__":
	g = Game()
	g.add_player("a")
	g.add_player("b")
	g.add_player("c")
	print(g.find_first_player())
	print(g.turn)
	print(g.get_player_turn())
	print(g.get_player_turn())






