import pyglet
import Game
from CardWindow import CardWindow

def cardwindowstarter(game):
	window = CardWindow(game, 1000, 800, "Monopoly", resizable=False)
	pyglet.app.run()
