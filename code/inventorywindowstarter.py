import pyglet
from InventoryScreen import InventoryWindow

def start_inventory_window(game, player):
	window = InventoryWindow(game, player, 1000, 800, "Monopoly", resizable=False) #inventory instance
	pyglet.app.run()