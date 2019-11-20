import PlayerDetailWindow
from pyglet.gl import *
from pyglet.window import key
import pyglet
from pyglet.gl import *
from pyglet.window import key

class PlayerUsernameWindow(pyglet.window.Window):

	#global players

	def __init__(self,  *args, **kwargs):
		super().__init__(*args, **kwargs)
		pyglet.gl.glClearColor(0.5, 0, 0, 1)
		self.set_location(100, 100)
		self.labels = []
		#self.players = players
		self.text_label = pyglet.text.Label("Enter a username player {}:".format(0),
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
		username = ""
		if symbol == key.A:
			username += "a"
		elif symbol == key.B:
			username += "b"
		elif symbol == key.C:
			username += "c"
		elif symbol == key.D:
			username += "d"
		elif symbol == key.E:
			username += "e"
		elif symbol == key.F:
			username += "f"
		elif symbol == key.G:
			username += "g"
		elif symbol == key.H:
			username += "h"
		elif symbol == key.I:
			username += "i"
		elif symbol == key.J:
			username += "j"
		elif symbol == key.K:
			username += "k"
		elif symbol == key.L:
			username += "l"
		elif symbol == key.M:
			username += "m"
		elif symbol == key.N:
			username += "n"
		elif symbol == key.O:
			username += "o"
		elif symbol == key.P:
			username += "p"
		elif symbol == key.Q:
			username += "q"
		elif symbol == key.R:
			username += "r"
		elif symbol == key.S:
			username += "s"
		elif symbol == key.T:
			username += "t"
		elif symbol == key.U:
			username += "v"
		elif symbol == key.V:
			username += "v"
		elif symbol == key.W:
			username += "w"
		elif symbol == key.X:
			username += "x"
		elif symbol == key.Y:
			username += "y"
		elif symbol == key.Z:
			username += "z"
		elif symbol == key.ENTER:
			print(username)
		print(username)
	