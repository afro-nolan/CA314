from PlayerPieceWindow import PlayerPieceWindow
import pyglet

def start_player_piece_window(username=""):
	playerpiecewindow = PlayerPieceWindow(username, 1000, 800, "Monopoly",resizable=False)
	pyglet.app.run()

if __name__ == "__main__":
	start_player_piece_window()