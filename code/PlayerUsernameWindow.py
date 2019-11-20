import PlayerDetailWindow
from pyglet.gl import *
from pyglet.window import key
import pyglet
from pyglet.gl import *
from pyglet.window import key
from playerpiecestarter import start_player_piece_window

class PlayerUsernameWindow(pyglet.window.Window):

	#global players

	def __init__(self,  *args, **kwargs):
		super().__init__(*args, **kwargs)
		pyglet.gl.glClearColor(0.5, 0, 0, 1)
		self.set_location(100, 100)
		self.labels = []
		#self.players = players
		self.text_label = pyglet.text.Label("Enter a username player {}:".format(1),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2-50,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.text_label)
		self.username = ""

	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		#self.background.draw()
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		self.close()

	def on_key_press(self, symbol, modifiers):
		if symbol == key.A:
			self.username += "a"
		elif symbol == key.B:
			self.username += "b"
		elif symbol == key.C:
			self.username += "c"
		elif symbol == key.D:
			self.username += "d"
		elif symbol == key.E:
			self.username += "e"
		elif symbol == key.F:
			self.username += "f"
		elif symbol == key.G:
			self.username += "g"
		elif symbol == key.H:
			self.username += "h"
		elif symbol == key.I:
			self.username += "i"
		elif symbol == key.J:
			self.username += "j"
		elif symbol == key.K:
			self.username += "k"
		elif symbol == key.L:
			self.username += "l"
		elif symbol == key.M:
			self.username += "m"
		elif symbol == key.N:
			self.username += "n"
		elif symbol == key.O:
			self.username += "o"
		elif symbol == key.P:
			self.username += "p"
		elif symbol == key.Q:
			self.username += "q"
		elif symbol == key.R:
			self.username += "r"
		elif symbol == key.S:
			self.username += "s"
		elif symbol == key.T:
			self.username += "t"
		elif symbol == key.U:
			self.username += "v"
		elif symbol == key.V:
			self.username += "v"
		elif symbol == key.W:
			self.username += "w"
		elif symbol == key.X:
			self.username += "x"
		elif symbol == key.Y:
			self.username += "y"
		elif symbol == key.Z:
			self.username += "z"
		elif symbol == key.ENTER or symbol == key.RETURN:
			pyglet.clock.schedule_once(self.exit_callback , 2)
			#Get their game piece
			start_player_piece_window(self.username)

	