import pyglet
from pyglet.window import key

window = pyglet.window.Window()
image  = pyglet.resource.image('resources/titledeed.jpg')

label = pyglet.text.Label("                                         Enter B or A" ,
                            font_name='Times New Roman',
                            font_size = 18,
                            x= window.width//2, y = window.height//2,
                            anchor_x = 'center', anchor_y ='center')



@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print("A Key was pressed")

    elif symbol == key.B:
        print("B key was pressed")

    elif symbol == key.ENTER:
        print("ENTER key was pressed")



@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0,0)


pyglet.app.run()







