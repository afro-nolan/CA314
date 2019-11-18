import pyglet
from main import main
from Help import Help
from pyglet.image.codecs.png import PNGImageDecoder
from pyglet.gl import *

class GameWindow(pyglet.window.Window):
	"""Represents the game window"""

	def __init__(self, *args, **kwargs):
		"""Initialises the game window"""
		super().__init__(*args, **kwargs)
		self.background = pyglet.graphics.Batch()
		#self.main_background = pyglet.sprite.Sprite(pyglet.image.load('resources/monopoly.jpg'), batch=self.background, x=0, y=0)
		#self.background.anchor_x = 500
		#self.background.anchor_y = 400
		#self.background.height=800
		self.set_location(100, 100)
		self.frame_rate = 1/60.0


	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		#self.clear()
		#for l in labels:
		#	l.draw()

		#glEnable(GL_BLEND)
		#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		#image.blit(0,0)
		#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		self.render()

	def render(self):
		self.clear()
		#self.background.draw()
		for l in labels:
			l.draw()
		#self.flip()

		#image.blit(self.width//2,self.height//2)

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