import pyglet

class PlayerPieceWindow(pyglet.window.Window):

	def __init__(self,username, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.username = username
		self.gamepiece = gamepiece
		pyglet.gl.glClearColor(0.5, 0, 0, 1)
		self.set_location(100, 100)
		self.labels = []
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.text_label = pyglet.text.Label("{} choose a gamepiece:".format(self.username.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
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
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		#self.background.draw()
		for l in self.labels:
			l.draw()
			print(self.username)

	def exit_callback(self, t):
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


