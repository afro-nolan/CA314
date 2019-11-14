from Card import Card


class TitleDeedCard(Card):

	def __init__(self, name, description, keep, cost, mortgage_price, rent, grouping, colour, house_price, hotel_price):
		super().__init__(self, name, description, keep)
		self.cost = cost
		self.mortgage_price = mortgage_price
		self.rent = rent
		self.grouping = grouping
		self.colour = colour
		self.house_price = house_price
		self.hotel_price = hotel_price

	def get_price(self):
		return self.cost

	def get_grouping(self):
		return self.grouping

	def get_mortgage_price(self):
		return self.mortgage_price

	def get_rent_price(self):
		return self.rent