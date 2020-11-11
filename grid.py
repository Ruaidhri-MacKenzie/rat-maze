# Ruaidhri MacKenzie 2020

class Grid:
	"""Class which represents a grid of values with methods to set values."""

	def __init__(self, columns, rows, default_value = 0):
		"""Create a matrix of nodes with a default value."""
		self.nodes = []
		for y in range(rows):
			self.nodes.append([])
			for _ in range(columns):
				self.nodes[y].append(default_value)
		self.width = len(self.nodes[0])
		self.height = len(self.nodes)
		self.default_value = default_value

	def __str__(self):
		"""Return a string representing the 2d grid."""
		text = ""
		for y in range(self.height):
			for x in range(self.width):
				text += str(self.nodes[y][x]) + " "
			text += '\n'
		return text

	def __len__(self):
		"""Return the number of nodes in the grid."""
		return self.width * self.height
	
	def indexToPosition(self, index):
		"""Return a 1d index from a 2d position."""
		x = index % self.width
		y = (index - x) / self.width
		return (x, y)
	
	def positionToIndex(self, x, y):
		"""Return a 2d position from a 1d index."""
		return (y * self.width) + x
	
	def getValue(self, x, y):
		"""Return the node value at a position."""
		return self.nodes[y][x]

	def setValue(self, x, y, value = 0):
		"""Set the node value at a position."""
		self.nodes[y][x] = value

	def getValueAtIndex(self, index):
		"""Return the node value at an index."""
		x, y = self.indexToPosition(index)
		return self.nodes[y][x]
	
	def setValueAtIndex(self, index, value = 0):
		"""Set the node value at an index."""
		x, y = self.indexToPosition(index)
		self.nodes[y][x] = value
	
	def resize(self, columns, rows):
		"""Resize the grid, adding blank columns and rows if required."""
		# Remove extra rows
		if self.height > rows:
			self.nodes = self.nodes[slice(rows)]

		for y in range(rows):
			# Remove extra columns
			if y > len(self.nodes):
				self.nodes[y] = self.nodes[y][slice(columns)]

			# Add new rows
			if y >= self.height:
				self.nodes.append([])

			for x in range(columns):
				# Add new columns
				if x >= len(self.nodes[y]):
					self.nodes[y].append(self.default_value)
		
		self.width = len(self.nodes[0])
		self.height = len(self.nodes)

	def fill(self, value):
		"""Set the value of every node in the grid."""
		for y in range(self.height):
			for x in range(self.width):
				self.setValue(x, y, value)
