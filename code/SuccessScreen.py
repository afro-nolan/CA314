import pyglet
from pyglet.gl import *
from pyglet.window import key
from Game import Game
from Inventory import Inventory
from Player import Player
#from main import start_player_details_window

class SuccessScreenWindow(pyglet.window.Window):
	"""Represents the game window"""

	def __init__(self, *args, **kwargs):
		"""Initialises the game window"""
		super().__init__(*args, **kwargs)
		self.background = pyglet.graphics.Batch()
		self.set_location(100, 100)
		self.frame_rate = 1/60.0
		self.image = pyglet.image.load("resources/success.jpg")
		self.image_sprite = pyglet.sprite.Sprite(self.image, x=60,y=160)

	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		self.image_sprite.draw()
		#sprite.draw()
		#self.background.draw()
		for l in labels:
			l.draw()

	def update(self, dt):
		"""Updates the window"""
		pass

	def exit_callback(self, t):
		self.close()

if __name__ == "__main__":
	window = SuccessScreenWindow(1000, 800, "Monopoly", resizable=False)
	#sprite = pyglet.sprite.Sprite(image, x=0, y=0
	winner = Game().get_winner()
	inventory = 0

	label = pyglet.text.Label("Player " + winner + " Wins!!", font_name="Times New Roman", 
			font_size = 40, x=window.width//1.9, y=window.height//1.28,
			anchor_x='center', anchor_y='center', color=(0,0,0,255))

	label2 = pyglet.text.Label("with €"+ str(inventory), font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height//2.75, anchor_x = 'center',
				anchor_y='center', color=(0,0,0,255))
	
	labels = [label, label2]
	pyglet.clock.schedule_once(window.exit_callback , 5) 
	pyglet.app.run()
	#start_player_details_window()
