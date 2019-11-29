from pyglet.window import key
import pyglet
from pyglet.gl import *
from pyglet.window import key
from main import start_player_details_window

class HelpMenuWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		pyglet.gl.glClearColor(0.5, 0, 0, 1) #Background colour
		self.set_location(100, 100) #Set the location of the window
		self.labels = []
		#Title label
		self.title_label = pyglet.text.Label('Monopoly Rules',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Main text
		self.rent_label = pyglet.text.Label("1. Collecting Rent: If another player lands on one of your unmortgaged properties, you are due rent from them as shown on the Title Deed Card.",
                         	font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-240,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.auction_label1 = pyglet.text.Label("2. Auction: An auction will be held when A) a player lands on an unowned property and decides not to buy it.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-270,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.auction_label2 = pyglet.text.Label("B) A player goes bankrupt and turns over all their unmortgaged properties to the Bank, which are auctioned unmortgaged",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.auction_label3 = pyglet.text.Label("C) There is a building shortage and more than one player wants to buy the same building.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-330,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.auction_label4 = pyglet.text.Label("A player can start the bidding price for as low as €1 and if no one makes a higher bid, the last player must buy the property.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-350,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.build_label1 = pyglet.text.Label("3. Build: When you own all the sites in a colour group, you can buy houses and put them on your sites. The price of the house is on the Title Deed Card",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-380,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.build_label2 = pyglet.text.Label("You must build evenly. You cannot build a second house on a site until you have build one on each site of its colour group. You can have max 4 houses.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-410,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.build_label3 = pyglet.text.Label("You can only have one hotel per site and cannot build additional houses on the site.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-440,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.cards_label1 = pyglet.text.Label("4. If you land on a card square, you will receive a card and you must follow the instruction on it, ff it is a Get Out Of Jail Free card you may keep it or sell it.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-470,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.cards_label2 = pyglet.text.Label("If you land on Income Tax or Super Tax, then you must pay the price shown.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-500,
                         	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.jail_label1 = pyglet.text.Label("If you land on the 'Go To Jail' space then you will be moved to Jail, without collecting €200 if you pass Go. Your turn will now end",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-530,
                         	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.jail_label2 = pyglet.text.Label("If you get a card telling you to Go To Jail or you roll 3 doubles in a row, then you must also go to jail. Ending your turn.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-560,
                         	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.win_label = pyglet.text.Label("The last player left in the game wins. Every other player will be bankrupt.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-210,
                         	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.first_label = pyglet.text.Label("To decide who goes first, each player will roll the dice and the player with the highest sum will go first.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-170,
                         	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.win_label)
		self.labels.append(self.rent_label)
		self.labels.append(self.auction_label1)
		self.labels.append(self.auction_label2)
		self.labels.append(self.auction_label3)
		self.labels.append(self.auction_label4)
		self.labels.append(self.build_label1)
		self.labels.append(self.build_label2)
		self.labels.append(self.build_label3)
		self.labels.append(self.cards_label1)
		self.labels.append(self.cards_label2)
		self.labels.append(self.jail_label1)
		self.labels.append(self.jail_label2)
		self.labels.append(self.first_label)

	def on_draw(self):
		"""Draws on the screen"""
		self.render()

	def render(self):
		"""Renders the screen"""
		#Clear screen
		self.clear()
		#Draw labels
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		"""Exit the window"""
		self.close()

	def on_key_press(self, symbol, modifier):
		"""Collect keypress from user"""

		#If user wants to exit help menu
		if symbol == key.RETURN or symbol == key.ENTER:
			start_player_details_window()

