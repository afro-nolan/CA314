import pyglet
from Help import Help
from pyglet.image.codecs.png import PNGImageDecoder
from pyglet.gl import *

class PlayerDetailWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.labels = []
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.set_location(100, 100)

	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		#self.background.draw()
		for l in self.labels:
			l.draw()

	#def on_key_press(symbol, modifiers):
	#	pass

