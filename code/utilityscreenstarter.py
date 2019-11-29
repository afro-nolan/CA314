import pyglet
from UtilityWindow import UtilityWindow

def utilityscreenstarter(game):
	window = UtilityWindow(game, 1000, 800, "Monopoly", resizable=False)
	pyglet.app.run()