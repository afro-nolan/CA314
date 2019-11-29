from pyglet.window import key
import pyglet
from gameboardstarterwindow import startgamewindow
from Game import Game
from Player import Player
from GamePiece import GamePiece

class PlayerColourWindow(pyglet.window.Window):
	"""Represents the PlayerColourWindow. Allows players to choose their colours"""

	def __init__(self, players, *args, **kwargs):
		"""Initialises the window. Takes a list of players as a parameter"""
		super().__init__(*args, **kwargs)
		pyglet.gl.glClearColor(0.5, 0, 0, 1) #Background colour
		self.set_location(100, 100) #Set the location of the window
		self.player_details = players #Initialise the list of players
		self.players = len(self.player_details) #Get the number of players in the game
		self.players_count = self.players #Count of players in the game
		self.colour = "" #Temporary colour holder
		self.labels = []
		#Title Label
		self.title_label = pyglet.text.Label('Monopoly',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Main text label
		self.text_label = pyglet.text.Label("{} choose a colour:".format(self.player_details[(self.players - self.players_count)][0].capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		#Colour labels
		self.red_label = pyglet.text.Label("Press 1 for red",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.yellow_label = pyglet.text.Label("Press 2 for yellow",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2 + 200, y=self.height//2-100,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.lightblue_label = pyglet.text.Label("Press 3 for light blue",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-150,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.green_label = pyglet.text.Label("Press 4 for green",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+200, y=self.height//2-150,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.pink_label = pyglet.text.Label("Press 5 for pink",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.purple_label = pyglet.text.Label("Press 6 for purple",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+200, y=self.height//2-200,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.navy_label = pyglet.text.Label("Press 7 for navy",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2-200, y=self.height//2-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.orange_label = pyglet.text.Label("Press 8 for orange",
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2+200, y=self.height//2-250,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.text_label)
		self.labels.append(self.red_label)
		self.labels.append(self.yellow_label)
		self.labels.append(self.lightblue_label)
		self.labels.append(self.green_label)
		self.labels.append(self.pink_label)
		self.labels.append(self.purple_label)
		self.labels.append(self.navy_label)
		self.labels.append(self.orange_label)

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

	def on_key_press(self, symbol, modifiers):
		"""Get users input from keyboard"""
		if symbol == key._1:
			self.colour = "red"
		elif symbol == key._2:
			self.colour = "yellow"
		elif symbol == key._3:
			self.colour = "lightblue"
		elif symbol == key._4:
			self.colour == "green"
		elif symbol == key._5:
			self.colour == "pink"
		elif symbol == key._6:
			self.color == "purple"
		elif symbol == key._7:
			self.colour == "navy"
		elif symbol == key._8:
			self.colour == "orange"
		#If player has chosent their colour
		elif symbol == key.ENTER or symbol == key.RETURN:
			#If there are more players left
			if self.players_count > 1:
				#Get player details and place in list player
				player = self.player_details[self.players - self.players_count]
				#Add colour to the players details
				player.append(self.colour)
				#Place the player list back in the player details
				self.player_details[self.players - self.players_count] = player
				#Reset the temporary colour holder
				self.colour = ""
				#Decrement the numbers of players left
				self.players_count -= 1
				#Remove the text label
				self.labels.pop(1)
				#Reset the text label with the next username
				self.text_label = pyglet.text.Label("{} choose a colour:".format(self.player_details[(self.players - self.players_count)][0].capitalize()),
                         	font_name='Times New Roman',
                         	font_size=36,
                         	x=self.width//2, y=self.height//2,
                          	anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
				#Place the label back into the labels list in the same position
				tmp_label = [self.labels[0]]
				tmp_label.append(self.text_label)
				tmp_label += self.labels[1:]
				self.labels = tmp_label
				self.render()
			#We are at the last player
			else:
				#Get player details and place in list player
				player = self.player_details[self.players - self.players_count]
				#Add colour to the players details
				player.append(self.colour)
				#Place the player list back in the player details
				self.player_details[self.players - self.players_count] = player
				#Set up game
				g = self.game_setup()
				#Close the window
				pyglet.clock.schedule_once(self.exit_callback , 2)
				#Start the game
				startgamewindow(g)

	def game_setup(self):
		"""Set Up Game"""
		game = Game() #Game instance
		#Create players
		for p in self.player_details:
			name = p[0]
			piece = p[1]
			piece = GamePiece(piece, 0)
			colour = p[2]
			player = Player(name, colour, piece, 0)
			#Add the player to the game
			game.add_player(player)

		#Initialise cards
		game.start_game()
		return game



