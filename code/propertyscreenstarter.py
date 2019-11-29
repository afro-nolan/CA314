import pyglet
from buyProperty import PropertyWindow

def propertyscreenstarter(game):
	screen = PropertyWindow(game, 1000, 800, "Monopoly", resizable=False)
	pyglet.app.run()
