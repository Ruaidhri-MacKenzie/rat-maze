from rat_maze import RatMaze
from rat_ai import RatAI

class RatMazeAI(RatMaze):
	def __init__(self):
		super().__init__(['r', 'R'], 3)
		self.path_char = '.'

	def update(self):
		for y in range(self.height):
			for x in range(self.width):
				if self.getValue(x, y) == self.path_char:
					self.setFloor(x, y)

		for rat in self.rats:
			rat.moveToNearestSprout(self)
			if rat.shortest_path:
				for x, y in rat.shortest_path:
					if self.isFloor(x, y):
						self.setValue(x, y, self.path_char)
					elif self.getValue(x, y) == self.path_char:
						self.setValue(x, y, ':')

	def addRat(self, char):
		"""Add a rat AI at a random floor node."""
		x, y = self.findRandomFloorNode()
		self.rats.append(RatAI(x, y, char))
		self.setValue(x, y, char)
