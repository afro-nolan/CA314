
class Bank:

	def __init__(self):
		self.money = 0
		self.houses = 0
		self.hotels = 0 
		self.properties = []
		self.cards = []

	def allocate_money(self):
		pass

	def get_house_count(self):
		return self.houses

	def get_hotel_count(self):
		return self.hotels

	def remove_property(self, property):
		properties.remove(property)
		return property

	def place_propery(property):
		self.properties.append(property)

	def place_card(self, card):
		self.cards.append(card)

	def remove_card(self, card):
		self.cards.remove(card)

	def auction(self, player, property):
		pass

	def mortgage_property(self, player, property):
		pass

	def check_bidders(self):
		pass

	def bidMade(self):
		pass