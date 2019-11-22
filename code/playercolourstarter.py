import pyglet
from PlayerColourWindow import PlayerColourWindow

def start_player_colour_window(username="", gamepiece=""):
	playercolourwindow = PlayerColourWindow(username, gamepiece, 1000, 800, "Monopoly",resizable=False)
	pyglet.app.run()

if __name__ == "__main__":
	start_player_colour_window()
