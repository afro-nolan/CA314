
class Inventory:
	"""A player's inventory, holds a player's item"""

	def __init__(self):
		"""Initiate the inventory"""
		self.properties = {} #Properties stored in a dictionary, keys are properties, values are mortgaged or unmortgaged
		self.cards = [] #List of cards
		self.wallet = 1500 #Player's money

	def place_property(self, property):
		"""Place the property in the inventory"""
		if property not in self.properties:
			self.properties[property] = "unmortgaged"

	def place_card(self, card):
		"""Place the card in the inventory"""
		self.cards.append(card)

	def get_properties(self):
		return self.properties

	def remove_property(self, property):
		"""Remove the property from the inventory"""
		self.properties.remove(property)

	def remove_card(self, card):
		"""Remove the card from the inventory"""
		self.cards.remove(card)

	def show_inventory(self):
		"""Show the inventory"""
		items = " ".join(self.properties) + " ".join(self.cards)
		return items

	def contains(self, item):
		"""Check if the item is in the inventory"""
		if item in self.properties or self.cards:
			return True
		else:
			return False

	def deposit(self, amount):
		"""Deposit money in the wallet"""
		self.wallet += amount

	def withdraw(self, amount):
		"""Withdraw money from the wallet"""
		self.wallet -= amount

	def check_balance(self):
		"""Check the balance of the balance"""
		return self.wallet

	def set_properties(self, inven):
		self.properties = inven

	def unmortgagedProperties(self):
		"""Check if there are any unmortgaged properties in the inventory"""
		for property in self.properties:
			if self.properties[property] == "unmortgaged":
				return True
		return False

