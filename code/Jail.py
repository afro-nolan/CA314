from Square import Square


class Jail(Square):
	"""Represents a jail square"""

	def __init__(self, location):
		"""Initialises a jail square"""
		super().__init__(self, location)
		self.prisoners = [] #List of prisoners in jail

	def get_location(self):
		"""Get the location of the jail"""
		return self.location

	def get_prisoners(self):
		"""Return the prisoners in the jail"""
		return "-".join(self.prisoners)

	def contains(self, prisoner):
		"""Check if a prisoner is in jail"""
		if prisoner in self.prisoners:
			return True

		else:
			return False

	def remove(self, prisoner):
		"""Free a prisoner from jail"""
		if self.contains(prisoner):
			self.prisoners.remove(prisoner)
		else:
			return None

	def add_prisoner(self, prisoner):
		"""Lock another prisoner up"""
		if not self.contains(prisoner):
			self.prisoners.append(prisoner)
		else:
			return None

