import pyglet
from pyglet.window import key
import sys

image  = pyglet.resource.image('titledeed.jpg')


class Press(pyglet.window.Window):

    def __init__(self,*args,**kwargs):
        pyglet.window.Window.__init__(self, *args,**kwargs)

        self.label = pyglet.text.Label("                                      Enter B or A" ,
                                font_name='Times New Roman',
                                font_size = 18,
                                x= self.width//2, y = self.height//2,
                                anchor_x = 'center', anchor_y ='center')

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            print("A Key was pressed")

        elif symbol == key.B:
            print("B key was pressed")

        elif symbol == key.ENTER:
            print("ENTER key was pressed") 

    def on_draw(self):
        print("The window was drawn")
        sys.stdout.flush()
        self.label.draw()
        image.blit(0,0)

press = Press()
pyglet.app.run()





