#from Game import Game
from Die import Die
from Game import Game
from Player import Player
import pyglet

def main():
	game = Game()
	p1 = Player("Aifric", "red", "ship", "Go")
	print(p1.get_name())
	p1.move()

if __name__ == "__main__":
	main()
