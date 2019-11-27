#when player presses 'c' to construct this menu will appear 

import pyglet
from pyglet.gl import *
from pyglet.window import key
from Inventory import Inventory
from Property import Property
# import bankruptcy screen, auction screen, mortgage screen, board screen

class GameWindow(pyglet.window.Window):
	"""Represents the game window"""

	def __init__(self, *args, **kwargs):
		"""Initialises the game window"""
		super().__init__(*args, **kwargs)
		self.background = pyglet.graphics.Batch()
		self.set_location(100, 100)
		self.frame_rate = 1/60.0
		self.option = ""

	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		image_sprite.draw()
		for l in labels:
			l.draw()

	def update(self, dt):
		"""Updates the window"""
		pass

	def exit_callback(self, t):
		self.close()

	def on_key_press(self, symbol, modifiers):
		"""Get users input from keyboard"""
		if symbol == key._1:
			self.option = "house"
		elif symbol == key._2:
			self.option = "hotel"
		elif symbol == key.ENTER or symbol == key.RETURN:
			if self.option == "hotel":
				# check that player owns all properties of a colour grouping and has 4 houses
				# on each property

			elif self.option == "house":
				#check player owns all properties of a colour group



if __name__ == "__main__":
	window = GameWindow(1000, 800, "Monopoly", resizable=False)

	image = pyglet.image.load("resources/house_hotel.png")
	image_sprite = pyglet.sprite.Sprite(image, x=200,y=300)

	label = pyglet.text.Label("Buy a house or hotel", font_name="Times New Roman", 
			font_size = 48, x=window.width//2, y=window.height -100,
			anchor_x='center', anchor_y='center', color=(255,255,255,255))

	label2 = pyglet.text.Label("Press '1' to buy a house or '2' to buy a hotel", font_name="Times New Roman", 
			font_size = 32, x=window.width//2, y=window.height-600,
			anchor_x='center', anchor_y='center', color=(255,255,255,255))

	labels = [label, label2]
	pyglet.gl.glClearColor(0.5, 0, 0, 1)
	pyglet.app.run()
