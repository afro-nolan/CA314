

class Bank:

	def __init__(self):
		self.money = 20,580
		self.houses = 0
		self.hotels = 0 
		self.properties = []
		self.cards = []

	def allocate_money(self, players):
		for player in players:
			if player.inventory.check_balance() == 0:
				player.inventory.deposit(1500)
			else:
				return
		
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

	def deposit(self, amount):
		self.money += amount

	def withdraw(self, amount):
		self.money -= amount

	def auction(self, player, property):
		pass

	def mortgage_property(self, player, property):
		#if the property is not already mortgaged
		if property.get_mortgage() == False:
			#mortgage the property
			property.mortgage()
			#get the mortgage price
			price = property.get_title_deed_card().get_mortgage_price()
			#give the player the mortgage money
			player.get_inventory().deposit(price)
			#withdraw the mortgage money from the bank
			self.withdraw(price)


	def check_bidders(self):
		pass

	def bidMade(self):
		pass