from pyglet.window import key
import pyglet

class PlayerColourWindow(pyglet.window.Window):
	"""Represents the card window"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.set_location(100, 100) #Set the location of the window

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


