import pyglet
from MainGameWindow import MainGameWindow

def startgamewindow(game):
	gamewindow = MainGameWindow(game, 1000, 800, "Monopoly", resizable=False)
	pyglet.app.run()


if __name__ == "__main__":
	startgamewindow()