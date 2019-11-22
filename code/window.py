import pyglet
from main import start_player_details_window
from Help import Help
from pyglet.image.codecs.png import PNGImageDecoder
from pyglet.gl import *
from pyglet.window import key
#from PlayerDetailWindow import PlayerDetailWindow

class GameWindow(pyglet.window.Window):
	"""Represents the game window"""

	def __init__(self, *args, **kwargs):
		"""Initialises the game window"""
		super().__init__(*args, **kwargs)
		self.background = pyglet.graphics.Batch()
		self.set_location(100, 100)
		self.frame_rate = 1/60.0


	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		#self.background.draw()
		for l in labels:
			l.draw()

	def update(self, dt):
		"""Updates the window"""
		pass

	def exit_callback(self, t):
		self.close()

	def on_key_press(self, symbol, modifiers):
		#If the user wants to start the game
		if symbol == key.S:
			#Kill this window after 2 seconds
			pyglet.clock.schedule_once(self.exit_callback , 2) 
			#Start the player detail window
			start_player_details_window()
		
		#If the user wants help
		elif symbol == key.H:
			rules = help_menu_starter()

if __name__ == "__main__":
	window = GameWindow(1000, 800, "Monopoly", resizable=False)
	title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=window.width//2, y=window.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
	start_label = pyglet.text.Label("Press 's' to start",
                         font_name='Times New Roman',
                         font_size=36,
                         x=window.width//2, y=window.height//2-100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
	help_label = pyglet.text.Label("Press 'h' for help",  
							font_name='Times New Roman',
                          	font_size=36,
                          	x=window.width//2, y=window.height // 2 - 200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
	labels = [title_label, start_label, help_label]
	pyglet.gl.glClearColor(0.5, 0, 0, 1)
	image = pyglet.image.load('resources/dance.png', decoder=PNGImageDecoder())
	image.anchor_x = window.width // 2
	image.anchor_y = window.height // 2
	pyglet.app.run()


