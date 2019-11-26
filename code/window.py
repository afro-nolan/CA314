#Monopoly game starter - Game is run from here. 

import pyglet
from main import start_player_details_window
from Help import Help
from pyglet.image.codecs.png import PNGImageDecoder
from pyglet.gl import *
from pyglet.window import key
from help_menu_starter import help_menu_window


class GameWindow(pyglet.window.Window):
	"""Represents the game window"""

	def __init__(self, *args, **kwargs):
		"""Initialises the game window"""
		super().__init__(*args, **kwargs)
		self.background = pyglet.graphics.Batch()
		self.set_location(100, 100)
		self.frame_rate = 1/60.0
		title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Start label
		start_label = pyglet.text.Label("Press 's' to start",
                         font_name='Times New Roman',
                         font_size=36,
                         x=self.width//2, y=self.height//2-100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Help label
		help_label = pyglet.text.Label("Press 'h' for help",  
							font_name='Times New Roman',
                          	font_size=36,
                          	x=self.width//2, y=self.height // 2 - 200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
			#List of labels
		self.labels = [title_label, start_label, help_label]
		pyglet.gl.glClearColor(0.5, 0, 0, 1) #Background colour


	def on_draw(self):
		"""Draws the game window. Receives labels in a list and draws each one"""
		self.render()

	def render(self):
		"""Renders the screen"""
		self.clear()
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		"""Closes the window"""
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
			#Kill this window after 2 seconds
			pyglet.clock.schedule_once(self.exit_callback , 2) 
			#Starts the help window
			help_menu_window()

if __name__ == "__main__":
	window = GameWindow(1000, 800, "Monopoly", resizable=False) #GameWindow instance
	#Title of screen
	title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=window.width//2, y=window.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
	#Start label
	start_label = pyglet.text.Label("Press 's' to start",
                         font_name='Times New Roman',
                         font_size=36,
                         x=window.width//2, y=window.height//2-100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
	#Help label
	help_label = pyglet.text.Label("Press 'h' for help",  
							font_name='Times New Roman',
                          	font_size=36,
                          	x=window.width//2, y=window.height // 2 - 200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
	#List of labels
	labels = [title_label, start_label, help_label]
	pyglet.gl.glClearColor(0.5, 0, 0, 1) #Background colour
	#image = pyglet.image.load('resources/dance.png', decoder=PNGImageDecoder()) #Image - doesn't work yet
	#image.anchor_x = window.width // 2 
	#image.anchor_y = window.height // 2
	pyglet.app.run() #Run the game


