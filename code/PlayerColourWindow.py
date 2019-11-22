from pyglet.window import key
import pyglet
from gameboardstarterwindow import startgamewindow

class PlayerColourWindow(pyglet.window.Window):

	def __init__(self, username, gamepiece, *args, **kwargs):
		super().__init__(*args, **kwargs)
		pyglet.gl.glClearColor(0.5, 0, 0, 1)
		self.set_location(100, 100)
		self.username = username
		self.gamepiece = gamepiece
		self.colour = ""
		self.labels = []
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.text_label = pyglet.text.Label("{} choose a colour:".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.red_label = pyglet.text.Label("Press 1 for red:".format(),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.yellow_label = pyglet.text.Label("Press 2 for yellow".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2 + 200, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.lightblue_label = pyglet.text.Label("Press 3 for light blue".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-150,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.green_label = pyglet.text.Label("Press 4 for green".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+200, y=self.height//2-150,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.pink_label = pyglet.text.Label("Press 5 for pink".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.purple_label = pyglet.text.Label("Press 6 for purple".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+200, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.navy_label = pyglet.text.Label("Press 7 for navy".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.orange_label = pyglet.text.Label("Press 8 for orange".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+200, y=self.height//2-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.text_label)
		self.labels.append(self.red_label)
		self.labels.append(self.yellow_label)
		self.labels.append(self.lightblue_label)
		self.labels.append(self.green_label)
		self.labels.append(self.pink_label)
		self.labels.append(self.purple_label)
		self.labels.append(self.navy_label)
		self.labels.append(self.orange_label)

	def on_draw(self):
		self.render()

	def render(self):
		self.clear()
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		self.close()

	def on_key_press(self, symbol, modifiers):
		"""Get users input from keyboard"""
		if symbol == key._1:
			self.colour = "red"
		elif symbol == key._2:
			self.colour = "yellow"
		elif symbol == key._3:
			self.colour = "lightblue"
		elif symbol == key._4:
			self.colour == "green"
		elif symbol == key._5:
			self.colour == "pink"
		elif symbol == key._6:
			self.color == "purple"
		elif symbol == key._7:
			self.colour == "navy"
		elif symbol == key._8:
			self.colour == "orange"
		elif symbol == key.ENTER or symbol == key.RETURN:
			print("{} {} {}".format(self.username, self.gamepiece, self.colour))
			#pyglet.clock.schedule_once(self.exit_callback , 2)
			#startgamewindow(self.username, self.gamepiece, self.colour)

	def add_player(self):
		"""Create a player instance and add them to the game"""
		pass



