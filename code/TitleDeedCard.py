from Card import Card


class TitleDeedCard(Card):

	def __init__(self, name, keep, cost, mortgage_price, rent, grouping, colour, house_price, hotel_price, img=""):
		super().__init__(self, name, keep)
		self.cost = cost
		self.mortgage_price = mortgage_price
		self.rent = rent
		self.grouping = grouping
		self.colour = colour
		self.house_price = house_price
		self.hotel_price = hotel_price
		self.image = img

	def get_price(self):
		return self.cost

	def get_grouping(self):
		return self.grouping

	def get_mortgage_price(self):
		return self.mortgage_price

	def get_rent_price(self):
		return self.rent

	def get_name(self):
		return self.name

	def get_image(self):
		return self.image