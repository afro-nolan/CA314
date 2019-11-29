import pyglet
import sys

class BankruptWindow(pyglet.window.Window):

    def __init__(self,*args,**kwargs):
        pyglet.window.Window.__init__(self, *args,**kwargs)

        self.label = pyglet.text.Label('Bankrupt!! Better Luck next time',
                          font_name='Times New Roman',
                          font_size=30,
                          x=self.width//2,
                          y=self.height//2,
                          anchor_x='center', anchor_y='center')

    def on_draw(self):
        print('The window was drawn!')
        sys.stdout.flush()
        self.label.draw()



TextWindow()
pyglet.app.run()
