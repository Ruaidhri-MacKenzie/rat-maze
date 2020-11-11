# Ruaidhri MacKenzie 2020

from maze import Maze
from rat import Rat

class RatMaze(Maze):
	"""Rat Maze game. Rats race around a maze for tasty sprouts."""

	def __init__(self, rat_chars, max_level):
		"""Create a random maze with sprouts and rats. Accepts a list of characters that represent each rat."""
		super().__init__(8, 8, ' ', '#')
		self.level = 1
		self.max_level = max_level

		# Define char to sprouts and sprout counter, then add a sprout
		self.sprout_char = '@'
		self.sprouts = 0
		self.addSprout()

		# Create empty list of rats and add a rat for each char in rat_chars
		self.rats = []
		for char in rat_chars:
			self.addRat(char)

	def isSprout(self, x, y):
		"""Return whether a position is a sprout."""
		return self.getValue(x, y) == self.sprout_char
	
	def addSprout(self):
		"""Add a sprout at a random floor node."""
		x, y = self.findRandomFloorNode()
		self.setValue(x, y, self.sprout_char)
		self.sprouts += 1
	
	def removeSprout(self, x, y, char):
		"""Remove a sprout from the maze. If no sprouts remain load the next level."""
		self.setValue(x, y, char)
		self.sprouts -= 1
		if self.sprouts <= 0:
			self.nextLevel()

	def isRat(self, x, y):
		"""Check a position for rats and return the character of the first found."""
		for rat in self.rats:
			if x == rat.x and y == rat.y:
				return rat.char
	
	def addRat(self, char):
		"""Add a rat at a random floor node."""
		x, y = self.findRandomFloorNode()
		self.rats.append(Rat(x, y, char))
		self.setValue(x, y, char)

	def moveRat(self, rat, direction):
		"""Move a rat in the given direction."""
		cur_x = dest_x = rat.x
		cur_y = dest_y = rat.y
		if direction == 'left':
			dest_x -= 1
		elif direction == 'right':
			dest_x += 1
		elif direction == 'up':
			dest_y -= 1
		elif direction == 'down':
			dest_y += 1

		# Check for walls, they are too high for rats to climb
		if not self.isWall(dest_x, dest_y):
			rat.move(direction)
			
			# Check for rats on the same node, or use floor otherwise
			char = self.isRat(cur_x, cur_y) or self.floor_char
			self.setValue(cur_x, cur_y, char)

			# Check for food on destination node
			if self.isSprout(dest_x, dest_y):
				rat.eat()
				self.removeSprout(dest_x, dest_y, rat.char)
				return	# Return so that rat char is not drawn on next level
			
			# Set rat char on new node unless next level is loaded
			# If this is ran after it appears on next level
			# If ran before checking for food it will overwrite the food char
			self.setValue(dest_x, dest_y, rat.char)

	def moveRatLeft(self, rat):
		"""Move a rat left."""
		self.moveRat(rat, 'left')

	def moveRatRight(self, rat):
		"""Move a rat right."""
		self.moveRat(rat, 'right')

	def moveRatUp(self, rat):
		"""Move a rat up."""
		self.moveRat(rat, 'up')

	def moveRatDown(self, rat):
		"""Move a rat down."""
		self.moveRat(rat, 'down')

	def nextLevel(self):
		"""Load the next level and reposition the rats."""
		self.level += 1

		if self.level > self.max_level:
			# Game over
			winner = self.rats[0]
			for rat in self.rats:
				if rat.meals > winner.meals:
					winner = rat
			print(f"{winner.char} wins with {winner.meals} points!")
			input()
			exit()

		# Create new maze
		size = (self.level + 1) * 4
		self.resize(size, size)

		# Add sprouts
		num_sprouts = (self.level * 2) - 1
		for _ in range(num_sprouts):
			self.addSprout()

		# Reposition rats
		for rat in self.rats:
			x, y = self.findRandomFloorNode()
			rat.setPosition(x, y)
			self.setValue(x, y, rat.char)
