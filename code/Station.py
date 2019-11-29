from TitleDeedCard import TitleDeedCard
from Square import Square
from Bank import Bank

class Station:

	def __init__(self, name, owned, owner, cost, title_deed_card, location):
		self.name = name
		self.owned = owned
		self.owner = owner
		self.cost = cost
		self.title_deed_card = title_deed_card
		self.location = location

	def get_price(self):
		return self.cost

	def get_location(self):
		return self.location

	def buy_station(self, player):
		if check_ownership() is False:
			player.inventory.place_card(self.title_deed_card)
			player.inventory.withdraw(self.cost)
			Bank.deposit(self.cost)
			set_owned(True)
			set_owner(player)
		else:
			pay_rent(player)

	def pay_rent(self, player):
		player.withdraw(self.get_rent())
		Bank.deposit(self.get_rent())

	def check_ownership(self):
		return self.owned

	def set_owner(self, player):
		self.owner = player

	def set_owned(self, own):
		self.owned = own

	def get_rent(self):
		return self.title_deed_card.get_rent_price()



