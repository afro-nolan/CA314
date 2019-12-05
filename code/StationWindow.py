import pyglet
from pyglet.window import key

class StationWindow(pyglet.window.Window):

	def __init__(self, game, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.game = game #game
		self.player = self.game.get_player_turn()
		pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
		self.set_location(100, 100) #Set the location of the window
		self.labels = []
		self.title_label = pyglet.text.Label("{} landed on a station".format(self.player.get_name().capitalize()),
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2, y=self.height//2+300,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		if self.player.get_square().check_ownership() == False:
			self.text_label = pyglet.text.Label("Press 'b' to buy or 'A' to auction",
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2, y=self.height//2+200,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#else:
		#	self.text_label = pyglet.text.Label("{} owns this station. You must pay them {} in rent.".format(self.player.get_square().get_owner(), self.player.get_square().get_rent()),
      #                      font_name='Times New Roman',
       #                     font_size=36,
       #                     x=self.width//2, y=self.height//2+200,
       #                     anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.text_label)
		self.labels.append(self.title_label)


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

	def on_key_press(self, symbol, modifiers):
		if symbol == key.ENTER or symbol == key.RETURN:
			from gameboardstarterwindow import startgamewindow
			pyglet.clock.schedule_once(self.exit_callback , 2)
			startgamewindow(self.game)
