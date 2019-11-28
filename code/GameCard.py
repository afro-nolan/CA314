from Card import Card

class GameCard(Card):

	def __init__(self, name, description, keep, type, cost, players, location):
		"""Initialise GameCard """
		super().__init__(name, description, keep)
		self.type = type
		self.cost = cost
		self.other_players = players
		self.location = location


	def get_instruction(self):
		"""Get instruction on card"""
		return self.description

	def get_type(self):
		"""Get cost of the card if it has one"""
		return self.cost

	def get_location(self):
		"""Gets the location to move to if it has one"""
		return self.location

	def follow_instruction(self, player):
		"""Follows instruction on card"""
		if self.get_type() == "Gain":
			self.gain_money(player)
		elif self.get_type() == "Lose":
			self.lose_money(player)
		elif self.get_type() == "Move":
			self.move_player(player)
		elif self.get_type() == "GetOutOfJail":
			self.get_jailfree_card(player)

	def get_players(self):
		"""Gets any other players involved in card"""
		return self.other_players

	def players_is_empty(self):
		"""Check if other players involved"""
		return len(self.get_players())

	def gain_money(self, card_player):
		"""Gives the player the money specified on the card"""
		#If other players are involved
		if not self.players_is_empty():
			#For each player
			for player in self.get_players():
				#Take money out of their inventory
				player.inventory.withdraw(self.get_cost())
				card_player.inventory.deposit(self.get_cost()) #Give i
		#Otherwise just give the player the money
		else:
			Bank.withdraw(self.get_cost())
			card_player.inventory.deposit(self.get_cost())

	def lose_money(self, card_player):
		"""Takes away the money specified on the card"""
		#If other players are involved
		if not self.players_is_empty():
			#For each player
			for player in self.get_players():
				#Withdraw the money from the player with the card
				card_player.inventory.withdraw(self.get_cost())
				player.inventory.deposit(self.get_cost()) #Deposit the money in the players wallet
		#Otherwise, just take put the money
		else:
			card_player.inventory.withdraw(self.get_cost())

	def move_player(self, card_player):
		"""Move the player a certain amount of spaces"""
		#card_player.move(self.get_moves())

	def get_jailfree_card(self, card_player):
		"""Get a get out of jail free card"""
		card_player.inventory.place_card(self)
