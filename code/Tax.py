from Square import Square


class Tax(Square):

	def __init__(self, name, location, price):
		"""Initialise tax square"""
		super().__init__(name, location)
		self.price = price

	def get_location(self):
		"""Get the location of the square"""
		return self.location

	def get_price(self):
		"""Get the tax cost of the square"""
		return self.price

	def pay_tax(self, player, bank):
		"""Play the tax of the square"""
		player.inventory.withdraw(self.get_price()) #Withdraw tax from the player's wallet
		bank.deposit(self.get_price()) #Deposit the tax in the bank
		print("in pay tax functoin")

