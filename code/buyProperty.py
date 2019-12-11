import pyglet
from pyglet.window import key
import sys
from Player import Player
from Property import Property


class PropertyWindow(pyglet.window.Window):
    """Representents property window"""

    def __init__(self, game, *args,**kwargs):
        """Initialises property window"""
        super().__init__(*args, **kwargs)
        self.game = game #game
        pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
        self.set_location(100, 100) #Set the location of the window
        self.labels = []
        self.player = game.get_turn() #get player whosed turn it is
        self.sq = self.player.get_square() #square player is on
        self.card  = pyglet.resource.image(self.sq.get_title_deed_card().get_image()) #title deed card
        #title label
        self.title_label = pyglet.text.Label("{} landed on {}".format(self.player.get_name().capitalize(), self.sq.get_name()),
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2, y=self.height//2+300,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        #Check if owned or unowned
        if self.sq.check_ownership() == False:
            #Text Label
            self.text_label = pyglet.text.Label("Press 'b' to buy or 'A' to auction",
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2, y=self.height//2+200,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        else:
            self.text_label = pyglet.text.Label("{} owns this property. You must pay them {} in rent.".format(self.player.get_square().get_owner(), self.player.get_square().get_rent()),
                            font_name='Times New Roman',
                            font_size=36,
                            x=self.width//2, y=self.height//2+200,
                            anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        self.labels.append(self.text_label)
        self.labels.append(self.title_label)


    def on_key_press(self, symbol, modifiers):
        """Get the users key press"""

        if symbol == key.A:
            from auctionScreen2 import AuctionWindow
            pyglet.clock.schedule_once(self.exit_callback , 2)
            AuctionWindow()

        #Player wants to buy the property
        elif symbol == key.B:
            #property is unowned
            if self.sq.check_ownership() == False:
                #Player has enough money
                if self.player.get_inventory().check_balance() >= self.sq.get_title_deed_card().get_price():
                    #Player buys property
                    self.sq.buy_property(self.player)
            #Else, pay the owner rent
            else:
                self.sq.pay_rent(self.player)


        elif symbol == key.ENTER or symbol == key.RETURN:
            from gameboardstarterwindow import startgamewindow
            pyglet.clock.schedule_once(self.exit_callback , 2)
            startgamewindow(self.game)


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




