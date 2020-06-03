from random import randint

DEPTH = 6
INF = 666

def initGame():
	global gameState
	gameState = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def getOpSide(side):
	if side == 'X':
		return 'O'
	else:
		return 'X'

def getPlayerSide():
	print("Rolling the dices...")
	global robotSide

	playerSide = randint(0, 1)
	if playerSide == 0:
		robotSide = 'X'
		print("You are playing with O's")
		return 'O'
	else:
		robotSide = 'O'
		print("You are playing with X's")
		return 'X'

def setChoice(x, y, choice):
	if gameState[x][y] == '-':
		gameState[x][y] = choice
		return True
	return False	

def updateAsPlayer(choice):
	if not choice.isdigit():
			print("Invalid Input!")
			return False
		
	elif int(choice) < 1 or int(choice) > 9:
		print("Input not in range!")
		return False
	
	else:
		(line, col) = getLineAndCol(choice)
		info = setChoice(line, col, getOpSide(robotSide))
		
		if info == False:
			print("Place already filled!")
			return False
		else:
			return True

def getNextPossibleMoves():
	possibleMoves = []

	for line in range(3):
		for col in range(3):
			if gameState[line][col] == '-':
				possibleMoves.append((line, col))
	return possibleMoves



def lineIsFull(line):
	if line[0] == '-':
		return False
	else:
		return line[0] == line[1] == line[2] 

def getMainDiagonal():
	return [gameState[i][i] for i in range(3)]

def getSecondDiagonal():
	return [gameState[i][2 - i] for i in range(3)]

def getTransposed():
	return [[gameState[j][i] for j in range(3)] for i in range(3)]

def hasEnded():
	transposedGameState = getTransposed()
	
	# check lines and columns
	for line in range(3):
		# lines
		if lineIsFull(gameState[line]):
			return (True, gameState[line][0])

		# columns
		if lineIsFull(transposedGameState[line]):
			return (True, transposedGameState[line][0])

	# check diagonals
	if lineIsFull(getMainDiagonal()) or lineIsFull(getSecondDiagonal()):
		return (True, gameState[1][1])

	# check draw
	for line in range(3):
		for col in range(3):
			if gameState[line][col] == '-':
				# it means it's not ended and it's not a draw
				return (False, '!')

	# it means it's a draw
	return (None, '!')

def getLineAndCol(choice):
	choice = int(choice)

	if (choice % 3 == 0):
		line = int(choice / 3) - 1
	else:			
		line = int(choice / 3)

	return (line, (choice - 1) % 3)


def printCurrentState():
	for line in range(0,3):
		print(*gameState[line])
		print()

def negamax(depth, side):
	info = hasEnded()

	# stop conditions
	if info[0] == None:
		return (-1, -1, 0)
	elif info[0] == True:
		# check sides
		if info[1] == side:
			return (-1, -1, INF)
		else:
			return (-1, -1, -INF)

	if depth == 0:
		return (-1, -1, 0)

	line = -1
	col = -1
	maxScore = -INF

	# go branch
	for nextMove in getNextPossibleMoves():
		# apply move
		gameState[nextMove[0]][nextMove[1]] = side
		
		# enter in recursivity
		fromBranch = negamax(depth - 1, getOpSide(side))

		# update maximum
		if (-fromBranch[2] >= maxScore):
			maxScore = -fromBranch[2]
			line = nextMove[0]
			col = nextMove[1]

		# restore
		gameState[nextMove[0]][nextMove[1]] = '-'
	
	return (line, col, maxScore)

def updateAsRobot():
	newMoveInfo = negamax(DEPTH, robotSide)

	setChoice(newMoveInfo[0], newMoveInfo[1], robotSide)
	