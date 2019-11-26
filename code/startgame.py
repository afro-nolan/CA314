from window import GameWindow
import pyglet

def start_game():
	window = GameWindow(1000, 800, "Monopoly", resizable=False) #GameWindow instance
	pyglet.app.run() #Run the game

if __name__ == "__main__":
	main()