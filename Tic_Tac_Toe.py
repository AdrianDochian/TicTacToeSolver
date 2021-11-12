# Tic Tac Toe game

from helpers import *

while True:
	playerSide = getPlayerSide()

	initGame()

	if playerSide == 'O':
		updateAsRobot()

	while True:
		printCurrentState()

		choice = input("Enter the place for input[1-9]: ")

		info = updateAsPlayer(choice)

		if info == False:
			continue
		
		# check if game has ended
		info = hasEnded()

		if info[0] == True or info[0] == None:
			break 

		# the robot responds
		updateAsRobot()

		# check if game has ended
		info = hasEnded()

		if info[0] == True or info[0] == None:
			break

	printCurrentState()

	if (info[0] == None):
		print("The game ended with a draw")
	else:
		if (info[1] == playerSide):
			print(f"You have won!")
		else:
			print(f"Robot has won!")

	ans = input("\nType \"exit\" to quit the game or anything else to play again: ")
	print()
	if ans == "exit":
		break