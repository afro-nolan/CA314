import pyglet
from main import main
from Help import Help

class GameWindow(pyglet.window.Window):
	"""Represents the game window"""

	def __init__(self, *args, **kwargs):
		"""Initialises the game window"""
		super().__init__(*args, **kwargs)
		self.set_location(100, 100)
		self.frame_rate = 1/60.0


	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.clear()
		for l in labels:
			l.draw()

	def update(self, dt):
		"""Updates the window"""
		pass

	def on_key_press(symbol, modifiers):
		if symbol == key.S:
			main()
		elif symbol == key.H:
			rules = help_menu()

if __name__ == "__main__":
	window = GameWindow(1000, 800, "Monopoly", resizable=False)
	title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=64,
                         x=window.width//2, y=window.height - 100,
                          anchor_x='center', anchor_y='center')
	start_label = pyglet.text.Label("Press 's' to start",
                         font_name='Times New Roman',
                         font_size=36,
                         x=window.width//2, y=window.height//2-100,
                          anchor_x='center', anchor_y='center')
	help_label = pyglet.text.Label("Press 'h' for help",  
							font_name='Times New Roman',
                          	font_size=36,
                          	x=window.width//2, y=window.height // 2 - 200,
                          	anchor_x='center', anchor_y='center')
	labels = [title_label, start_label, help_label]
	pyglet.app.run()