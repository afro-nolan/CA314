import PlayerDetailWindow
from pyglet.gl import *
from pyglet.window import key
import pyglet
from pyglet.gl import *
from pyglet.window import key
from playerpiecestarter import start_player_piece_window

class PlayerUsernameWindow(pyglet.window.Window):
	"""Represents the window to get all the players user names"""

	def __init__(self, players,  *args, **kwargs):
		"""Initialises the player username window"""
		super().__init__(*args, **kwargs)
		#Number of players playing the game
		self.players = players
		#Background colour
		pyglet.gl.glClearColor(0.5, 0, 0, 1)
		self.set_location(100, 100) #Location of the window
		self.labels = []
		self.player_count = self.players #Count of players in game
		#Title label
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                         anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Main text
		self.text_label = pyglet.text.Label("Enter a username player {}:".format(self.players - (self.player_count) + 1),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2-50,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.text_label)
		self.names = [] #List of names
		self.username = "" #Temporary username holder

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
		"""Closes the window"""
		self.close()

	def on_key_press(self, symbol, modifiers):
		"""Gets keypress from user"""
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
		#If user is done typing their username
		elif symbol == key.ENTER or symbol == key.RETURN:
			#If there are still more players to get
			if self.player_count > 1:
				#Add the name to the name list
				self.names.append(self.username)
				#Decrement count
				self.player_count -= 1
				#Reset temporary username holder
				self.username = ""
				#Remove the text label
				self.labels.pop()
				#Reset with new player
				self.text_label = pyglet.text.Label("Enter a username player {}:".format(self.players - (self.player_count) + 1),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2-50,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
				self.labels.append(self.text_label)
				self.render()
			#We are at the last player
			else:
				#Add the name to the name list
				self.names.append(self.username)
				self.player_count -= 1
				#Set the window to close after 2 seconds
				pyglet.clock.schedule_once(self.exit_callback , 2)
				#Go to gamePiece window to let users choose gamepieces
				start_player_piece_window(self.names, self.players)

	