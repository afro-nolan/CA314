import pyglet
from pyglet.gl import *
from pyglet.window import key
from Inventory import Inventory
# import bankruptcy screen, auction screen, mortgage screen, board screen

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
		for l in labels:
			l.draw()

	def update(self, dt):
		"""Updates the window"""
		pass

	def exit_callback(self, t):
		self.close()

	def on_key_press(self, symbol):
		if symbol == key.S:
			pyglet.clock.schedule_once(self.exit_callback, 2)
			#sell screen

		elif symbol == key.B:
			pyglet.clock.schedule_once(self.exit_callback, 2)
			#bankruptcy screen

		elif symbol == key.M:
			pyglet.clock.schedule_once(self.exit_callback, 2)
			#mortgage screen

		elif symbol == key.RETURN or symbol == key.ENTER:
			pyglet.clock.schedule_once(self.exit_callback , 2)
			#board screen

if __name__ == "__main__":
	window = GameWindow(1000, 800, "Monopoly", resizable=False)

	wallet = Inventory().wallet

	p = Inventory().properties
	prop = ""
	for key, value in p.items():
		prop += key + "(" + value + "), "

	c = Inventory().cards
	cards = ""
	for card in c:
		cards += card + ", "

	label = pyglet.text.Label("Inventory", font_name="Times New Roman", 
			font_size = 48, x=window.width//2, y=window.height-100,
			anchor_x='center', anchor_y='center', color=(255,255,255,255))

	wallet_label = pyglet.text.Label("Money: €" + str(wallet), font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-200, anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	prop_label = pyglet.text.Label("Properties: " + prop, font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-250,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	card_label = pyglet.text.Label("Cards: " + cards, font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-300,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	mort_label = pyglet.text.Label("Press 'm' to mortgage", font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-600,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	sell_label = pyglet.text.Label("Press 's' to sell", font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-550,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	bankr_label = pyglet.text.Label("Press 'b' for bankruptcy", font_name="Times New Roman", font_size = 28,
				x=window.width//2, y=window.height-500,anchor_x = 'center',
				anchor_y='center', color=(255,255,255,255))

	labels = [label, wallet_label, prop_label, card_label, mort_label, sell_label, bankr_label]
	pyglet.gl.glClearColor(0.5, 0, 0, 1)
	pyglet.app.run()
