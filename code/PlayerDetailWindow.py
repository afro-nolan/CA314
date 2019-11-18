import pyglet
from Help import Help
from pyglet.image.codecs.png import PNGImageDecoder
from pyglet.gl import *
from pyglet.window import key

class PlayerDetailWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.labels = []
		pyglet.gl.glClearColor(0.5, 0, 0, 1)
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.num_players_label = pyglet.text.Label("Enter the number of players between 2-8",
                         font_name='Times New Roman',
                         font_size=36,
                         x=self.width//2, y=self.height//2-50,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.num_players_label)
		self.set_location(100, 100)
		pyglet.gl.glClearColor(0.5, 0, 0, 1)
		self.players = 0

	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		#self.background.draw()
		for l in self.labels:
			l.draw()

	def on_key_press(self, symbol, modifiers):
		players = self.get_players()
		if symbol == key._2:
			players = 2
		elif symbol == key._3:
			players = 3
		elif symbol == key._4:
			players = 4
		elif symbol == key._5:
			players = 5
		elif symbol == key._6:
			players = 6
		elif symbol == key._7:
			players = 7
		elif symbol == key._8:
			players = 8
		self.update_players(players)
		self.get_player_details()

	def get_players(self):
		"""Get player count"""
		return self.players

	def update_players(self, amount):
		self.players = amount

	def get_labels(self):
		return self.labels

	def pop_labels(self):
		self.labels.pop()

	def get_player_details(self):
		"""Get details for each player"""
		print(self.labels)
		self.pop_labels()

		for i in range(1, self.get_players()+1):
			print(i)
			player = pyglet.text.Label("Player {}".format(i),
                         font_name='Times New Roman',
                         font_size=36,
                         x=self.width//2, y=self.height//2-50,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
			self.on_draw()
			self.get_player_details().append(player)


