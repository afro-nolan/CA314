from pyglet.window import key
import pyglet
from pyglet.gl import *
from pyglet.window import key

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
		self.rent_label = pyglet.text.Label("Collecting Rent: If another player lands on one of your unmortgaged properties, you are due rent from them as shown on the Title Deed Card.",
                         	font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.auction_label1 = pyglet.text.Label("Auction: An auction will be held when 1) a player lands on an unowned property and decides not to buy it.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.auction_label2 = pyglet.text.Label("2) A player goes bankrupt and turns over all their unmortgaged properties to the Bank, which are auctioned unmortgaged, 3) There is a building shortage and more than one player wants to buy the same building. A player can start the bidding price for as low as €1 and if no one makes a higher bid, the last player must buy the property.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.auction_label3 = pyglet.text.Label(" 3) There is a building shortage and more than one player wants to buy the same building. A player can start the bidding price for as low as €1 and if no one makes a higher bid, the last player must buy the property.",
							font_name='Times New Roman',
                         	font_size=10,
                         	x=self.width//2, y=self.height-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.rent_label)
		self.labels.append(self.auction_label)

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

