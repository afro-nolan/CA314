import pyglet
from pyglet.window import key
from playercolourstarter import start_player_colour_window

class PlayerPieceWindow(pyglet.window.Window):
	"""Represents the window to let users choose their game pieces"""

	def __init__(self, names, players, *args, **kwargs):
		"""Initialise the class. Takes a list of names and a count of players"""
		super().__init__(*args, **kwargs)
		self.names = names
		self.players = players
		self.gamepiece = "" #Temporary gamepiece holder
		self.players_count = self.players #Count of players in game
		self.player_details = [] #List for storing player details
		pyglet.gl.glClearColor(0.5, 0, 0, 1) #Background colour
		self.set_location(100, 100)
		self.labels = []
		self.taken = [] #Game pieces taken
		#Title label
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Main text label
		self.text_label = pyglet.text.Label("{} choose a gamepiece:".format(self.names[(self.players - self.players_count)].capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Game Piece labels
		self.ship_label = pyglet.text.Label("Press 1 for ship",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2-200, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.car_label = pyglet.text.Label("Press 2 for car",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2 + 200, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.dog_label = pyglet.text.Label("Press 3 for dog",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2 - 200, y=self.height//2-150,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.wheel_label = pyglet.text.Label("Press 4 for wheelbarrow",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2 + 200, y=self.height//2-150,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.iron_label = pyglet.text.Label("Press 5 for iron",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2 - 200, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.hat_label = pyglet.text.Label("Press 6 for hat",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2 + 200, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.thimble_label = pyglet.text.Label("Press 7 for thimble",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2 - 200, y=self.height//2-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.boot_label = pyglet.text.Label("Press 8 for boot",
							font_name='Times New Roman',
                         	font_size=30,
                         	x=self.width//2 + 200, y=self.height//2-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.text_label)
		self.labels.append(self.ship_label)
		self.labels.append(self.car_label)
		self.labels.append(self.dog_label)
		self.labels.append(self.wheel_label)
		self.labels.append(self.iron_label)
		self.labels.append(self.hat_label)
		self.labels.append(self.thimble_label)
		self.labels.append(self.boot_label)

	def on_draw(self):
		"""Draw the screen"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		"""Close the window"""
		self.close()

	def on_key_press(self, symbol, modifier):
		"""Get users input from keyboard"""
		if symbol == key._1:
			self.gamepiece = "ship"
		elif symbol == key._2:
			self.gamepiece = "car"
		elif symbol == key._3:
			self.gamepiece = "dog"
		elif symbol == key._4:
			self.gamepiece == "wheel"
		elif symbol == key._5:
			self.gamepiece == "iron"
		elif symbol == key._6:
			self.gamepiece == "hat"
		elif symbol == key._7:
			self.gamepiece == "thimble"
		elif symbol == key._8:
			self.gamepiece == "boot"
		#User has chosen their piece
		elif symbol == key.ENTER or symbol == key.RETURN:
			#If there are more players to go through
			if self.players_count > 1:
				#Get the name of the player
				pname = self.names[(self.players - self.players_count)]
				#Store the name and gamepiece in an array p
				p = [pname, self.gamepiece]
				#Append p to the player details array
				self.player_details.append(p)
				#Reset temporary gamepiece holder
				self.gamepiece = ""
				#Decrement players count
				self.players_count -= 1
				#Remove main text label
				self.labels.pop(1)
				#Reset label with next players username
				self.text_label = pyglet.text.Label("{} choose a gamepiece:".format(self.names[(self.players - self.players_count)].capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
				#Place label back in in the same position
				tmp_label = [self.labels[0]]
				tmp_label.append(self.text_label)
				tmp_label += self.labels[1:]
				self.labels = tmp_label
				self.render()
			#We are at the last player
			else:
				#Get the name of the player
				pname = self.names[(self.players - self.players_count)]
				#Store the name and gamepiece in an array p
				p = [pname, self.gamepiece]
				#Append p to the player details array
				self.player_details.append(p)
				#Close the window after two seconds
				pyglet.clock.schedule_once(self.exit_callback , 2)
				#Go to playercolour window to allow users to choose their colours
				start_player_colour_window(self.player_details) 


