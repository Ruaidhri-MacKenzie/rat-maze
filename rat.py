# Ruaidhri MacKenzie 2020

class Rat:
	"""Rat class for running around mazes and eating."""

	def __init__(self, x, y, char = 'r'):
		"""Create a rat with x and y positions, a character to represent it, and a meals counter."""
		self.char = char
		self.x = x
		self.y = y
		self.meals = 0

	def __str__(self):
		"""Return the char representing the rat."""
		return self.char
	
	def setPosition(self, x, y):
		"""Set the x and y positions of the rat."""
		self.x = x
		self.y = y
	
	def move(self, direction):
		"""Move the rat in the given direction."""
		if direction == 'left':
			self.moveLeft()
		elif direction == 'right':
			self.moveRight()
		elif direction == 'up':
			self.moveUp()
		elif direction == 'down':
			self.moveDown()

	def moveLeft(self):
		"""Move the rat left."""
		self.x -= 1

	def moveRight(self):
		"""Move the rat right."""
		self.x += 1

	def moveUp(self):
		"""Move the rat up."""
		self.y -= 1

	def moveDown(self):
		"""Move the rat down."""
		self.y += 1
	
	def eat(self):
		"""Eat some food."""
		self.meals += 1

	def poop(self):
		"""Everybody poops."""
		if self.meals > 0:
			self.meals -= 1
		else:
			pass # wind
