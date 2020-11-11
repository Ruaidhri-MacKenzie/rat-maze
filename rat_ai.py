from rat import Rat

class RatAI(Rat):
	def __init__(self, x, y, char):
		super().__init__(x, y, char)
		self.shortest_path = None

	def checkForSprout(self, maze, x, y, path):
		if (x, y) in path or maze.isWall(x, y):
			return

		path.append((x, y))

		if maze.isSprout(x, y):
			if not self.shortest_path or len(path) < len(self.shortest_path):
				self.shortest_path = path.copy()
		else:
			if x > 0:
				self.checkForSprout(maze, x - 1, y, path)
			if x < maze.width - 1:
				self.checkForSprout(maze, x + 1, y, path)
			if y > 0:
				self.checkForSprout(maze, x, y - 1, path)
			if y < maze.height - 1:
				self.checkForSprout(maze, x, y + 1, path)

		path.pop()

	def moveToNearestSprout(self, maze):
		if not self.shortest_path:
			self.checkForSprout(maze, self.x, self.y, [])
		
		if self.shortest_path:
			target_x, target_y = self.shortest_path[-1]
			x, y = self.shortest_path.pop(0)

			if maze.isSprout(target_x, target_y):
				if x < self.x:
					maze.moveRat(self, 'left')
				elif x > self.x:
					maze.moveRat(self, 'right')
				elif y < self.y:
					maze.moveRat(self, 'up')
				elif y > self.y:
					maze.moveRat(self, 'down')
			else:
				self.shortest_path = None
