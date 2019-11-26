from GameCard import GameCard
from Game import Game

def set_game_cards(self):
	##Pseudocode for game card
	gamecards = {}
	players = Game.get_players() #Instances of the players in the game. You can get this from the Game class.

	gc1 = GameCard("Chance Card", "It's your birthday! Collect €10 from each player!", False, "gain", 10, players, 0)