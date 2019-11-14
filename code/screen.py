import pyglet
from pyglet_gui.theme import Theme

theme = Theme({"font": "Lucida Grande",
               "font_size": 12,
               "text_color": [255, 0, 0, 255]}, resources_path='')

window = pyglet.window.Window()
label = pyglet.text.Label("Monopoly", font_name="Times New Roman", 
		font_size = 36, x=window.width//2, y=window.height//2,
		anchor_x='center', anchor_y='center')
		#create the window

@window.event
def on_draw():
	window.clear()
	label.draw()


pyglet.app.run()

