import pyglet
from PlayerDetailWindow import PlayerDetailWindow
#from window import GameWindow

def start_player_details_window():
	playerdetailswindow = PlayerDetailWindow(1000, 800, "Monopoly", resizable=False)
	pyglet.app.run()
