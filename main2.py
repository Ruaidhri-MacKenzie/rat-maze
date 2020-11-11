# Ruaidhri MacKenzie 2020

import time
from rat_maze_ai import RatMazeAI as Maze

def main():
	"""Game for AI rats. The rats navigates a maze to find tasty sprouts."""
	maze = Maze()

	# Game Loop
	while True:
		maze.update()
		print("=== Rat Maze AI ===\n")
		print(maze)
		print(f"\t\t\t\t\t{maze.rats[0].char} - Sprouts: {maze.rats[0].meals}\t\t{maze.rats[1].char} - Sprouts: {maze.rats[1].meals}")
		time.sleep(1)

if __name__ == "__main__":
	main()
