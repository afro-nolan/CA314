#from Game import Game
from Die import Die
from Game import Game
from Player import Player
import pyglet
from PlayerDetailWindow import PlayerDetailWindow
#from window import GameWindow

def start_player_details_window():
	playerdetailswindow = PlayerDetailWindow(1000, 800, "Monopoly", resizable=False)
	pyglet.app.run()
