from PlayerUsernameWindow import PlayerUsernameWindow
import pyglet


def start_player_username_window(players = 2):
	playerusernamewindow = PlayerUsernameWindow(players, 1000, 800, "Monopoly",resizable=False)
	pyglet.app.run()

if __name__ == "__main__":
	start_player_username_window(2)