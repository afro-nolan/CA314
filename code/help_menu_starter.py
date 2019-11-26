from HelpMenuWindow import HelpMenuWindow
import pyglet

def help_menu_window():
	help = HelpMenuWindow(1000, 800, "Monopoly",resizable=False)
	pyglet.app.run()

if __name__ == "__main__":
	help_menu_window()