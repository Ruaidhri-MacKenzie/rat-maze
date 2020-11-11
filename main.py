# Ruaidhri MacKenzie 2020

from rat_maze import RatMaze as Maze

def main():
	"""Game for 2 players. Each player controls a rat as they race around a maze finding tasty sprouts."""
	maze = Maze(['r', 'R'], 3)
	player1 = maze.rats[0]
	player2 = maze.rats[1]

	# Game Loop
	while True:
		print("=== Rat Maze ===\n")
		print(maze)
		print("\t\t\t\tr = (w, a, s, d)\tR = (i, j, k, l)\tq to Quit")
		print(f"\t\t\t\tSprouts: {player1.meals}\t\tSprouts: {player2.meals}")
		print()

		key = input("\t\t\t\tPlease enter a direction to move in: ").strip().lower()
		print()

		if key == 'a':			# Player 1 Left
			maze.moveRatLeft(player1)
		elif key == 'd':		# Player 1 Right
			maze.moveRatRight(player1)
		elif key == 'w':		# Player 1 Up
			maze.moveRatUp(player1)
		elif key == 's':		# Player 1 Down
			maze.moveRatDown(player1)
		elif key == 'j':		# Player 2 Left
			maze.moveRatLeft(player2)
		elif key == 'l':		# Player 2 Right
			maze.moveRatRight(player2)
		elif key == 'i':		# Player 2 Up
			maze.moveRatUp(player2)
		elif key == 'k':		# Player 2 Down
			maze.moveRatDown(player2)
		elif key == 'q':		# Quit
			confirm = input("\t\t\t\tAre you sure you want to quit? (y, n): ").strip().lower()
			if 'y' in confirm:
				break

if __name__ == "__main__":
	main()
