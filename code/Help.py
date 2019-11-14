
class Help():
	"""Represents a help class"""

	def __init__(self, filename):
		"""Initiates the help class, takes in a file name of game rules"""
		self.filename = filename
		self.rules = []

	def show_rules():
		"""returns the formatted rules"""
		return "\n".join(self.rules)

	def read_rules(self):
		"""Reads the rules from the file and inserts them in a list"""
		with open(self.filename) as f:
			self.rules = f.readlines()




