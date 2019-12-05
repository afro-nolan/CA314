import pyglet 
from StationWindow import StationWindow
from Game import Game

def stationscreenstarter(game):
	window = StationWindow(game, 1000, 800, "Monopoly", resizable=False)
	pyglet.app.run()