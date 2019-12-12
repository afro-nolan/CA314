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

	def get_utility_cost(self, roll, num_owned):
		"""Get cost of utilities for rent"""
		#If the player owns one utility
		if num_owned == 1:
			price = roll * 4
		#If the player owns two utilities
		elif num_owned == 2:
			price = roll * 10
		return price
