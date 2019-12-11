from Bank import Bank

class Property:

	def __init__(self, name, title_deed_card, location, owned, owner):
		"""Initiate Property"""
		self.name = name
		self.title_deed_card = title_deed_card #Title Deed Card
		self.location = location #Location of property
		self.houses = 0 #Count of houses on property
		self.hotels = 0 #Count of hotels on property
		self.owned = owned #Boolean Value representing if the property if owned
		self.owner = owner #Player who owns the property or None

	def get_location(self):
		"""Get the location of the property"""
		return self.location

	def get_houses(self):
		"""Get the houses count"""
		return self.houses

	def get_title_deed_card(self):
		return self.title_deed_card

	def get_hotels(self):
		"""Get the hotels count"""
		return self.hotels

	def buy_house(self, player):
		"""Buy a house for the property"""
		#If the hotel count is less than 4, then the player can purchase
		if self.get_houses() < 4:
			player.inventory.withdraw(self.title_deed_card.get_house_price()) #Charge the player
			Bank.deposit(self.title_deed_card.get_house_price()) #Deposit the money in the bank
			self.house += 1 #Increment the house count
		#Otherwise, the player cannot purchase
		else:
			return False

	def sell_house(self, player):
		"""Sell the house"""
		#If the houses count is 0, then they can purchase
		if self.get_houses() == 0:
			Bank.withdraw(self.title_deed_card.get_house_price()) #Take the money out of the bank
			player.inventory.deposit(self.title_deed_card.get_house_price()) #Deposit the money in the players wallet
			self.house -= 1 #Decrement the house count
		#Otherwise, the user can't buy
		else:
			return False

	def buy_hotel(self, player):
		"""Function to buy a hotel"""
		#If there are no hotels on the property, the player can buy
		if self.hotel == 0:
			player.inventory.withdraw(self.title_deed_card.get_hotel_price()) #Charge the player
			Bank.deposit(self.title_deed_card.get_hotel_price()) #Deposit the money from the bank
			self.hotel += 1 #Increment the hotel count

	def sell_hotel(self, player):
		"""Sell a hotel"""
		Bank.withdraw(self.title_deed_card.get_hotel_price()) #Withdraw the money from the bank
		player.inventory.deposit(self.title_deed_card.get_hotel_price()) #Deposit the money in the players wallet
		self.hotel -= 1 #Decrement the hotel count

	def buy_property(self, player, bank):
		"""Buy a property for a player"""
		#If the property is unowned
		if self.owned is False:
			player.inventory.withdraw(self.title_deed_card.get_price()) #Charge the player
			bank.deposit(self.title_deed_card.get_price()) #Deposit the money 
			self.set_owner(player) #Set the player as the owner
			self.set_owned(True) #Set the owned value to True
			player.inventory.place_property(self.title_deed_card) #Place the card in the player's inventory
		else:
			self.pay_rent()
			return False

	def pay_rent(self, player, owner):
		"""Make the player pay rent"""
		self.player.inventory.withdraw(get_rent()) #Withdraw rent from the players wallet
		self.owner.inventory.deposit(get_rent()) #Deposit the rent in the owners wallet 

	def get_rent(self):
		return self.title_deed_card.get_rent_price()

	def built_evenly(self):
		pass

	def check_ownership(self):
		return self.owned

	def ask_to_buy(self, player):
		if player.wants_to_buy(answer):
			return True
		else:
			return False

	def set_owner(self, player):
		self.owner = player

	def set_owned(self, own):
		self.owned = own

	def get_owner(self):
		return self.owner

	def get_name(self):
		return self.name


