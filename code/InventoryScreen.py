import pyglet
from pyglet.gl import *
from pyglet.window import key
from Inventory import Inventory
from Game import Game
from Player import Player

# import bankruptcy screen, auction screen, mortgage screen, board screen

class InventoryWindow(pyglet.window.Window):
	"""Represents the game window"""

	def __init__(self, game, player, *args, **kwargs):
		"""Initialises the game window"""
		super().__init__(*args, **kwargs)
		pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
		self.set_location(100, 100) #Set location on screen
		self.game = game #Game object
		#player's turn
		self.player = player
		#Get players wallet
		self.wallet = self.player.inventory.check_balance()
		#Labels
		self.labels = []
		self.properties = self.player.inventory.properties
		#Inventory label
		self.title_label = pyglet.text.Label("Inventory", 
				font_name="Times New Roman", 
				font_size = 48, x=self.width//2, y=self.height-100,
				anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.wallet_label = pyglet.text.Label("Money: €{}".format(self.wallet), 
				font_name="Times New Roman", font_size = 28,
				x=180, y=self.height-200, 
				anchor_x = 'center', anchor_y='center', color=(0, 0, 0, 255))
		self.properties_label = pyglet.text.Label("Properties: {}".format(len(self.properties)), 
				font_name="Times New Roman", font_size = 28,
				x=self.width//2+300, y=self.height-200,
				anchor_x = 'center', anchor_y='center', color=(0, 0, 0, 255))
		self.show_property_label = None
		self.labels.append(self.title_label)
		self.labels.append(self.wallet_label)
		self.labels.append(self.properties_label)
		self.get_property_count()

	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		self.close()

	def get_property_count(self):
		if len(self.properties) < 1:
			self.show_property_label = pyglet.text.Label("You have no properties!", 
						font_name="Times New Roman", font_size = 28,
						x=self.width//2, y=self.height//2,
						anchor_x = 'center', anchor_y='center', color=(0, 0, 0, 255))
			self.labels.append(self.show_property_label)
		else:
			start_height = self.width // 2
			i = 0
			for property in self.properties:
				pname = property.title_deed_card.get_name()
				if self.properties[property] != "mortgaged":
					prop_label = pyglet.text.Label("{}".format(pname), 
							font_name="Times New Roman", font_size = 28,
							x=start_height + i, y=self.height//2,
							anchor_x = 'center', anchor_y='center', color=(0, 0, 0, 255))
				else:
					prop_label = pyglet.text.Label("{} - mortgaged".format(pname), 
							font_name="Times New Roman", font_size = 28,
							x=start_height + i, y=self.height//2,
							anchor_x = 'center', anchor_y='center', color=(0, 0, 0, 255))
				i += 30
				self.labels.append(prop_label)

	def on_key_press(self, symbol, modifiers):
		#Go back to game screen
		if symbol == key.RETURN or symbol == key.ENTER:
			from gameboardstarterwindow import startgamewindow
			pyglet.clock.schedule_once(self.exit_callback , 2)
			startgamewindow(self.game)
		if symbol == key.S:
			self.option = "s"

		elif symbol == key.B:
			self.option = "b"

		elif symbol == key.M:
			self.option = "m"

	#	elif symbol == key.RETURN or symbol == key.ENTER:
	#		if self.option == "s":
	#			pyglet.clock.schedule_once(self.exit_callback , 2)
	#			# sell screen
	#		elif self.option == "b":
	#			pyglet.clock.schedule_once(self.exit_callback , 2)
				# bankrupt screen
	#		elif self.option == "m":
	#			pyglet.clock.schedule_once(self.exit_callback , 2)
				# mortgage screen

if __name__ == "__main__":
	window = GameWindow(1000, 800, "Monopoly", resizable=False)

	wallet = Inventory().wallet

	p = Inventory().properties
	prop = ""
	for key, value in p.items():
		prop += key + "(" + value + "), "

	c = Inventory().cards
	cards = ""
	for card in c:
		cards += card + ", "

	label = pyglet.text.Label("Inventory", font_name="Times New Roman", 
			font_size = 48, x=window.width//2, y=window.height-100,
			anchor_x='center', anchor_y='center', color=(255,255,255,255))

	wallet_label = pyglet.text.Label("Money: €" + str(wallet), font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-200, anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	prop_label = pyglet.text.Label("Properties: " + prop, font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-250,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	card_label = pyglet.text.Label("Cards: " + cards, font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-300,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	mort_label = pyglet.text.Label("Press 'm' to mortgage", font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-600,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	sell_label = pyglet.text.Label("Press 's' to sell", font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-550,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	bankr_label = pyglet.text.Label("Press 'b' for bankruptcy", font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-500,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	labels = [label, wallet_label, prop_label, card_label, mort_label, sell_label, bankr_label]
	pyglet.gl.glClearColor(0.5, 0, 0, 1)
	pyglet.app.run()
