import pyglet
from PlayerColourWindow import PlayerColourWindow

def start_player_colour_window(player_details=[]):
	"""Helper function to Start the PlayerColourWindow"""
	playercolourwindow = PlayerColourWindow(player_details, 1000, 800, "Monopoly",resizable=False)
	pyglet.app.run()

if __name__ == "__main__":
	start_player_colour_window()
