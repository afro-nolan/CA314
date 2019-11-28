from pyglet.window import key
import pyglet

class MainGameWindow(pyglet.window.Window):
	"""Main Game Window"""

	def __init__(self, game, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.game = game #game
		pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
		self.set_location(100, 100) #Set the location of the window
		self.board_image = pyglet.image.load("resources/monboard.jpeg")
		self.labels = []
		self.wallet_label = pyglet.text.Label("{}'s Wallet: {}".format("Aifric's", 0),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+300, y=self.height//2 + 300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.player_turn = pyglet.text.Label("It is {}'s turn.".format("Aifric"),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=180, y=self.height//2-300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.help_label = pyglet.text.Label("Press 'h' for help",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+300, y=self.height//2 + 100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.inventory_label = pyglet.text.Label("Press 'i' for inventory",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+270, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.roll_label = pyglet.text.Label("Press 'r' to roll",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+300, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.deal_label = pyglet.text.Label("Press 'd' to do a deal",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+270, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.quit_label = pyglet.text.Label("Press 'q' to quit",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+300, y=self.height//2-300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.wallet_label)
		self.labels.append(self.player_turn)
		self.labels.append(self.help_label)
		self.labels.append(self.inventory_label)
		self.labels.append(self.roll_label)
		self.labels.append(self.deal_label)
		self.labels.append(self.quit_label)


	def on_draw(self):
		"""Draws on the screen"""
		self.render()

	def render(self):
		"""Renders the screen"""
		#Clear screen
		self.clear()
		self.board_image.blit(0, self.height // 2 - 200)
		#Draw labels
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		"""Exit the window"""
		self.close()
