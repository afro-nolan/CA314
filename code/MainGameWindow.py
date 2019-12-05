from pyglet.window import key
import pyglet
import Game
from inventorywindowstarter import start_inventory_window
from propertyscreenstarter import propertyscreenstarter
import time
from cardwindowstarter import cardwindowstarter
from utilityscreenstarter import utilityscreenstarter
from stationscreenstarter import stationscreenstarter
from Property import Property
from CardSquare import CardSquare
from UtilitySquare import UtilitySquare
from FreeParking import FreeParking
from GoToJail import GoToJail
from Station import Station
from Tax import Tax

class MainGameWindow(pyglet.window.Window):
	"""Main Game Window"""

	def __init__(self, game, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.game = game #game
		#pyglet.gl.glClearColor(0.3,0.2,0.7, 1) #Background colour
		pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
		self.set_location(100, 100) #Set the location of the window
		self.board_image = pyglet.image.load("resources/monboard.jpeg")
		self.labels = []
		#Get player's turn
		self.player = self.game.get_player_turn()
		
		self.wallet_label = pyglet.text.Label("{}'s Wallet: €{}".format(self.player.name.capitalize(), self.player.inventory.check_balance()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+280, y=self.height//2 + 300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.player_turn = pyglet.text.Label("It is {}'s turn.".format(self.player.name.capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=180, y=self.height//2-300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.help_label = pyglet.text.Label("Press 'h' for help",
                         	font_name='Times New Roman',
                         	font_size=24,
                         	x=self.width//2+300, y=self.height//2 + 100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.inventory_label = pyglet.text.Label("Press 'i' for inventory",
                         	font_name='Times New Roman',
                         	font_size=24,
                         	x=self.width//2+270, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.roll_label = pyglet.text.Label("Press 'r' to roll",
                         	font_name='Times New Roman',
                         	font_size=24,
                         	x=self.width//2+300, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.deal_label = pyglet.text.Label("Press 'd' to do a deal",
                         	font_name='Times New Roman',
                         	font_size=24,
                         	x=self.width//2+270, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.quit_label = pyglet.text.Label("Press 'q' to quit",
                         	font_name='Times New Roman',
                         	font_size=24,
                         	x=self.width//2+300, y=self.height//2-300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.next_move_label = pyglet.text.Label("Press 'f' to finish your turn.",
								font_name='Times New Roman',
                         		font_size=24,
                         		x=self.width//2+300, y=self.height//2-330,
                          		anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.action_label = pyglet.text.Label("Action: {}".format("The game has started."),
								font_name='Times New Roman',
                         		font_size=18,
                         		x=200, y=self.height//2+300,
                          		anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.wallet_label)
		self.labels.append(self.player_turn)
		self.labels.append(self.help_label)
		self.labels.append(self.inventory_label)
		self.labels.append(self.roll_label)
		self.labels.append(self.deal_label)
		self.labels.append(self.quit_label)
		self.labels.append(self.action_label)


	def on_draw(self):
		"""Draws on the screen"""
		self.render()

	def render(self):
		"""Renders the screen"""
		#Clear screen
		self.clear()
		self.board_image.blit(0, self.height // 2 - 200)
		#Draw labels
		for l in self.labels:
			l.draw()

	def exit_callback(self, t=0):
		"""Exit the window"""
		self.close()

	def on_key_press(self, symbol, modifier):
		"""Get user's key press"""
		#If user presses 'q', they want to quit
		if symbol == key.Q:
			self.labels.pop()
			self.action_label = pyglet.text.Label("Action: {}".format("Quitting game."),
								font_name='Times New Roman',
                         		font_size=18,
                         		x=210, y=self.height//2+300,
                          		anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
			self.labels.append(self.action_label)
			pyglet.clock.schedule_once(self.exit_callback , 2)

		#Is user wants to see their inventory
		if symbol == key.I:
			pyglet.clock.schedule_once(self.exit_callback , 2)
			start_inventory_window(self.game, self.player)

		#User rolls the dice
		if symbol == key.R:
			#Get the sum of the dice
			amount = self.player.move()
			self.get_square()
			#Update the action message
			self.labels.pop()
			self.action_label = pyglet.text.Label("Action: {} rolled a {}.".format(self.player.get_name().capitalize(), amount),
								font_name='Times New Roman',
                         		font_size=18,
                         		x=210, y=self.height//2+300,
                          		anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
			self.labels.append(self.action_label)
			self.labels.pop()
			self.action_label = pyglet.text.Label("Action: {} lands on {}.".format(self.player.get_name().capitalize(), self.player.get_square().name),
								font_name='Times New Roman',
                         		font_size=18,
                         		x=210, y=self.height//2+300,
                          		anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
			self.labels.append(self.action_label)
			self.check_landing()


	def get_square(self):
		"""Get the square the user is on"""
		for sq in self.game.board.squares:
			if sq.location == self.player.get_location():
				self.player.set_square(sq)

	def check_landing(self):
		#Square player has landed on
		sq = self.player.get_square()
		#print("{} - {}".format(sq.get_name(), self.player.square.get_name()))
		#If it is a property, go to property square
		if isinstance(sq, Property):
			#Close the window
			pyglet.clock.schedule_once(self.exit_callback , 2)
			propertyscreenstarter(self.game)

		#If it is a tax square, pay tax
		elif isinstance(sq, Tax):
			sq.pay_tax(self.player, self.game.get_bank())
			self.labels.pop(0)
			self.wallet_label = pyglet.text.Label("{}'s Wallet: €{}".format(self.player.name.capitalize(), self.player.inventory.check_balance()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+300, y=self.height//2 + 300,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
			self.labels[0] = self.wallet_label

		#If it is a card square
		elif isinstance(sq, CardSquare):
			#Close the window
			pyglet.clock.schedule_once(self.exit_callback , 2)
			cardwindowstarter(self.game)

		#If it is a utility
		elif isinstance(sq, UtilitySquare):
			pyglet.clock.schedule_once(self.exit_callback, 2)
			utilityscreenstarter(self.game)

		#If it is a station
		elif isinstance(sq, Station):
			pyglet.clock.schedule_once(self.exit_callback, 2)
			stationscreenstarter(self.game)

		#If it is go to jail 
		elif isinstance(sq, GoToJail):
			pass

		#If it is jail or free parking
		else:
			return













