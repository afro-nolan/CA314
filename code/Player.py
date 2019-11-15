from Inventory import Inventory
from Die import Die
from Bank import Bank

class Player:

	def __init__(self, name, colour, piece, location):
		"""Initialises Player"""
		self.name = name #name of player
		self.colour = colour #Player's colour
		self.piece = piece #Player's piece
		self.inventory = Inventory() #Player's inventory
		self.location = location #Location of Player's GamePiece. This is a tuple
		self.dice = Die() #Player's Dice
		self.square = square #This is the square the player is on
		self.in_bid = False #Is the player bidding in an auction
		self.playing = True #Is the player still playing?

	def get_name(self):
		"""return the name of the player"""
		return self.name

	def do_deal(self, player, player_items, own_items):
		"""Do a deal with a player. Takes a player that they are dealing with and a list of items to trade"""
		#If the other player agrees to the deal
		if player.deal_agreed():
			#Loop through array
			for item in own_items:
				#If the item is a property then place it in the other's inventory
				if is_instance(item, Property):
					player.inventory.place_property(item)
				#If the item is a card, then place it in the other's inventory
				elif is_instance(item, Card):
					player.inventory.place_card(card)
				else:
					#Otherwise, it is money deposit it
					player.inventory.deposit(item)
			#Iterate through the other players items 
			for item in player_items:
				#Is the item a Property, if so remove it from their inventory
				if is_instance(player_items, Property):
					self.inventory.remove_property(item)
				#If the item is a Card, then remove it from their inventory
				elif is_instance(item, Card):
					self.inventory.remove_card(card)
				#Otherwise it is money, so we withdraw it from their inventory
				else:
					self.inventory.withdraw(item)
		#The player didn't agree, see if they want to counter or reject 
		else:
			if player.deal_countered():
				player.counter(self, player.items, self.items)
			elif player.reject_deal():
				return False
		

	def move(self, moves=None):
		"""Move the player's game piece"""
		if move is None:
			moves = self.dice.roll()
			self.location += moves
		else:
			self.location += moves
		pos_on_board = self.get_location() #Tuple position for square on board
		self.piece.update_position(pos_on_board[0], pos_on_board[1]) #Update game piece


	def get_location(self):
		"""Get the location of the player"""
		return self.location

	def get_square(self):
		"""Return the square the user is on"""
		return self.square

	def set_initial_bid(self, bid):
		return bid

	def make_bid(self, bid):
		self.in_bid = True

	def quit_bid(self):
		self.in_bid = False

	def get_in_bid(self):
		return self.in_bid

	def deal_agreed(self, agree):
		"""Takes a boolean 'agree' which if true, then the deal is agreed otherwise it is not"""
		return agree

	def deal_countered(self, counter):
		"""Takes a boolean, If the deal has been countered, then get them to choose the deal"""
		return counter

	def reject_deal(self, reject):
		return reject

	def counter(self, player, player_items, own_items):
		do_deal(player, player_items, own_items)

	def want_to_buy(self, answer):
		if answer is False:
			return False
		else:
			return True

	def stop_playing(self):
		self.playing = False

