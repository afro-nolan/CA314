from Card import Card

def GameCard(Card):

	def __init__(self, name, description, keep, type, cost, players, moves):
		"""Initialises the GameCard"""
		super().__init__(name, description, keep) #Takes attributes from parent class
		self.type = type #Classification of card, can be (gain money, lose money, move player)
		self.cost = cost
		self.other_players = self.players
		self.moves = self.moves

	def get_instruction(self):
		"""Gets the card instrucction"""
		return self.description

	def get_type(self):
		"""Gets the type of card, chance / community chest"""
		return self.type

	def get_cost(self):
		"""Gets the cost of the card if it has one"""
		return self.cost

	def get_moves(self):
		"""Gets the number of moves on the if it has them"""
		return self.moves

	def follow_instruction(self, player):
		"""Finds the instruction of the card"""
		if get_type() == "Gain":
			self.gain_money(player)
		elif get_type() == "Lose":
			self.lose_money(player)
		elif get_type() == "Move":
			self.move_player(player)
		elif get_type() == "GetOutOfJail":
			self.get_jailfree_card(player)

	def get_players(self):
		"""Gets any other players involved with the card"""
		return self.other_players

	def players_is_empty(self):
		"""Checks if there are any other players involved"""
		return len(self.other_players) == 0

	def gain_money(self, card_player):
		"""Gives the player the money specified on the card"""
		#If other players are involved
		if not self.players_is_empty():
			#For each player
			for player in self.get_players():
				#Take money out of their inventory
				player.inventory.withdraw(self.get_cost())
				card_player.inventory.deposit(self.get_cost()) #Give it to the player with the card
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
				card_player.inventory..withdraw(self.get_cost())
				player.inventory.deposit(self.get_cost()) #Deposit the money in the players wallet
		#Otherwise, just take put the money
		else:
			card_player.inventory.withdraw(self.get_cost())

	def move_player(self, card_player):
		"""Move the player a certain amount of spaces"""
		card_player.move(self.get_moves())

	def get_jailfree_card(self, card_player):
		"""Get a get out of jail free card"""
		Bank.cards.remove(self)
		card_player.inventory.place_card(self)




			

		