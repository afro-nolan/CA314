import pyglet
from pyglet.window import key

class UtilityWindow(pyglet.window.Window):

	def __init__(self, game, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.game = game #game
		pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
		self.set_location(100, 100) #Set the location of the window
		self.labels = []
		self.player = self.game.get_turn() #get player whosed turn it is
		self.sq = self.player.get_square() #square player is on
		self.card = pyglet.resource.image(self.sq.get_title_deed_card().get_image()) #title deed card
		#Title Label
		self.title_label = pyglet.text.Label('{} landed on an Utility'.format(self.player.get_name().capitalize()),
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		if self.player.get_square().check_ownership() == False:
			self.text_label = pyglet.text.Label("Press 'b' to buy or 'A' to auction",
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2, y=self.height//2+200,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)
		self.labels.append(self.text_label)


	def on_draw(self):
		"""Draws on the screen"""
		self.render()

	def render(self):
		"""Renders the screen"""
		#Clear screen
		self.clear()
		#Draw labels
		for l in self.labels:
			l.draw()
		self.card.blit(0,0)

	def exit_callback(self, t):
		"""Exit the window"""
		self.close()

	def on_key_press(self, symbol, modifier):
		if symbol == key.ENTER or symbol == key.RETURN:
			from gameboardstarterwindow import startgamewindow
			pyglet.clock.schedule_once(self.exit_callback , 2)
			startgamewindow(self.game)
		elif symbol == key.B:
		#property is unowned
			if self.sq.check_ownership() == False:
			#Player has enough money
				if self.player.get_inventory().check_balance() >= self.sq.get_title_deed_card().get_price():
					#Player buys property
					self.sq.buy_property(self.player, self.bank)
			#Else, pay the owner rent
			else:
				#get the number of utilities the player owns
				num_owned = self.get_utilities()
				#get the roll amount of the player
				roll = self.game.get_amount()
				#get utility price
				price = self.sq.get_title_deed_card().get_utility_cost(roll, num_owned)
				self.sq.pay_rent(self.player, self.sq.get_owner())

	def get_utilities(self):
		"""Get the number of utilities the player owns"""
		#get properties
		properties = self.sq.get_owner().get_inventory().get_properties()
		utility_count = 0 #utility count

		#iterate through properties
		for prop in properties:
			#if the properties are a utility and unmortgaged
			if prop.get_title_deed_card().get_grouping() == "E" and properties[prop] == "unmortgaged":
				utility_count += 1
		return utility_count


