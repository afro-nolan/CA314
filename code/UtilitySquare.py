from Square import Square

class UtilitySquare(Square):

	def __init__(self, name, location, title_deed_card, cost):
		super().__init__(name, location)
		self.cost = cost
		self.owned = False
		self.owner = False
		self.title_deed_card = title_deed_card


	def get_price(self):
		return self.cost

	def get_location(self):
		return self.location

	def get_name(self):
		return self.name

	def buy_utility(self, player):
		if check_ownership() is False:
			player.inventory.place_card(self.title_deed_card)
			player.inventory.withdraw(self.cost)
			Bank.deposit(self.cost)
			set_owned(True)
			set_owner(player)
		else:
			pay_rent(player)

	def pay_rent(self, player):
		player.withdraw(self.title_deed_card.rent)
		Bank.deposit(self.title_deed_card.rent)

	def check_ownership(self):
		return self.owned

	def set_owner(self, player):
		self.owner = player

	def set_owned(self, own):
		self.owned = own

		