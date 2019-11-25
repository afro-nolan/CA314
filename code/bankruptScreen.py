import pyglet
from pyglet_gui.theme import Theme

# t = Theme({"font": "Lucida Grande",
#             "font_size": 12,
#             "text_color": [255, 0, 0, 255]}, resources_path='')

window = pyglet.window.Window()

theme = Theme({"font": "Lucida Grande",
               "font_size": 12,
               "text_color": [255, 0, 0, 255]}, resources_path='')

label = pyglet.text.Label("Bankrupt!! Better Luck next time",
							font_name='Times New Roman',
							font_size = 30,
							x= window.width /2, y = window.height/2,
							anchor_x = 'center', anchor_y ='center')

@window.event
def on_draw():
	window.clear()
	label.draw()


pyglet.app.run()