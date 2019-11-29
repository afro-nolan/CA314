from Square import Square

class GoToJail(Square):

	def __init__(self, name, location):
		super().__init__(name, location)

	def get_name(self):
		return self.name

	def get_location(self):
		return self.location