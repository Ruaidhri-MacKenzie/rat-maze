# Ruaidhri MacKenzie 2020

import random
from grid import Grid

class Maze(Grid):
	"""Random maze generator."""

	def __init__(self, columns, rows, floor_char, wall_char):
		"""Create a random maze and store the display characters."""
		super().__init__(columns, rows, None)
		self.floor_char = floor_char
		self.wall_char = wall_char
		self.create()

	def isWall(self, x, y):
		"""Return whether a position is a wall node."""
		return self.getValue(x, y) == self.wall_char
	
	def isFloor(self, x, y):
		"""Return whether a position is a floor node."""
		return self.getValue(x, y) == self.floor_char
	
	def setWall(self, x, y):
		"""Set a position as a wall node."""
		self.setValue(x, y, self.wall_char)
	
	def setFloor(self, x, y):
		"""Set a position as a floor node."""
		self.setValue(x, y, self.floor_char)
	
	def findRandomFloorNode(self):
		"""Return the position of a random floor node."""
		x = random.randint(0, self.width - 1)
		y = random.randint(0, self.height - 1)
		while not self.isFloor(x, y):
			x = random.randint(0, self.width - 1)
			y = random.randint(0, self.height - 1)
		return (x, y)

	def countAdjacentFloorNodes(self, x, y):
		"""Return the number of adjacent nodes which are floors."""
		return self.isFloor(x - 1, y) + self.isFloor(x + 1, y) + self.isFloor(x, y - 1) + self.isFloor(x, y + 1)

	def resize(self, columns, rows):
		"""Creates a new maze of a specified size."""
		super().resize(columns, rows)
		self.fill(None)
		self.create()

	def create(self):
		"""Creates a maze using Randomized Prim's Algorithm."""
		# Pick a random starting position not on the parameter
		x = random.randint(1, self.width - 2)
		y = random.randint(1, self.height - 2)

		# Set node as floor and adjacent nodes as walls
		self.setFloor(x, y)
		self.setWall(x - 1, y)
		self.setWall(x + 1, y)
		self.setWall(x, y - 1)
		self.setWall(x, y + 1)

		# Create list of wall positions
		self._walls = []
		self._walls.append((x - 1, y))
		self._walls.append((x + 1, y))
		self._walls.append((x, y - 1))
		self._walls.append((x, y + 1))
		
		while self._walls:
			# Pick random wall position
			x, y = random.choice(self._walls)

			# Check if this node divides an empty node and a floor node
			if (x > 0 and x < self.width - 1) and (y > 0 and y < self.height - 1):
				if ((self._isEmpty(x - 1, y) and self.isFloor(x + 1, y))
				or (self._isEmpty(x + 1, y) and self.isFloor(x - 1, y))
				or (self._isEmpty(x, y - 1) and self.isFloor(x, y + 1))
				or (self._isEmpty(x, y + 1) and self.isFloor(x, y - 1))):
					# Check there are less than 2 adjacent floor nodes
					if self.countAdjacentFloorNodes(x, y) < 2:
						# Set current node as a floor
						self.setFloor(x, y)

						# Set adjacent empty tiles to walls and add to list of wall positions
						if x > 0:
							self._makeWall(x - 1, y)
						if x < self.width - 1:
							self._makeWall(x + 1, y)
						if y > 0:
							self._makeWall(x, y - 1)
						if y < self.height - 1:
							self._makeWall(x, y + 1)

			# Remove the current position from the list of wall positions
			for wall in self._walls:
				if (wall[0] == x and wall[1] == y):
					self._walls.remove(wall)
		
		# Fill in any empty nodes as walls
		for y in range(self.height):
			for x in range(self.width):
				if self._isEmpty(x, y):
					self.setWall(x, y)
	
	def createEntrances(self):
		"""Create entrance points at the top-left and bottom-right of the maze."""
		for x in range(self.width):
			if self.isFloor(x, 1):
				self.setFloor(x, 0)
				break
		for x in range(self.width - 1, 0, -1):
			if self.isFloor(x, self.height - 2):
				self.setFloor(x, self.height - 1)
				break
	
	def _isEmpty(self, x, y):
		"""Return whether a position is an empty node."""
		return self.getValue(x, y) == None
	
	def _makeWall(self, x, y):
		"""Set the position as a wall and add to the wall positions list."""
		if self._isEmpty(x, y):
			self.setWall(x, y)
			if (x, y) not in self._walls:
				self._walls.append((x, y))
