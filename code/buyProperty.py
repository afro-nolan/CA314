import pyglet
from pyglet.window import key
import sys


class PropertyWindow(pyglet.window.Window):

    def __init__(self, game, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.game = game #game
        pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
        self.set_location(100, 100) #Set the location of the window
        self.labels = []
        self.card  = pyglet.resource.image('resources/titledeed.jpg')
        self.player = game.get_turn()
        print(self.player.get_name())
        self.title_label = pyglet.text.Label("{} landed on {}".format(self.player.get_name(), self.player.get_square().get_name()),
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2+300, y=self.height//2 + 300,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        self.text_label = pyglet.text.Label("Press 'b' to buy or 'A' to auction",
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2+300, y=self.height//2 + 400,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        self.labels.append(self.text_label)
        self.labels.append(self.title_label)


    def on_key_press(self, symbol, modifiers):
        """Get the users key press"""
        if symbol == key.A:
            print("A Key was pressed")

        elif symbol == key.B:
            print("B key was pressed")

        elif symbol == key.ENTER:
            print("ENTER key was pressed") 

    def on_draw(self):
        """Draw the screen"""
        self.render()

    def render(self):
        """Render the screen"""
        self.clear()
        for l in self.labels:
            l.draw()
        self.card.blit(0,0)

    def exit_callback(self, t=0):
        """Exit the window"""
        self.close()




