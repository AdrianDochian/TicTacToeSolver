from random import randint

# fetch words
f = open ("words.in", "r")

words = []

for line in f:
	words.append(line.rstrip('\n'))

while True:
	print("Starting a new game...\n")

	# choose a word for this game
	rand = randint(0, len(words) - 1)
	numberOfHiddenChars = int(len(words[rand]) / 3) + 1

	hiddenPos = []

	while numberOfHiddenChars != 0:
		randPosInWord = randint(0, len(words[rand]) - 1)

		if randPosInWord in hiddenPos:
			continue
		else:
			hiddenPos.append(randPosInWord)
			numberOfHiddenChars -= 1

	chancesLeft = 8

	while hiddenPos != [] and chancesLeft != 0:
		print("\nChances left: {}".format(chancesLeft))

		for i in range(0, len(words[rand])):
			print(i, end = " ")
		
		print()	

		for i in range(0, len(words[rand])):
			if i in hiddenPos:
				print("_", end = " ")
			else:
				print(words[rand][i], end = " ")
		

		letter = input("\n\nChoose a letter: ")

		flagGoodGuess = 0
		for pos in hiddenPos:
			if words[rand][pos] == letter:
				print("Good guess!")
				hiddenPos.remove(pos)
				flagGoodGuess = 1
				break

		if flagGoodGuess == 0:
			print("Wrong guess!")
			chancesLeft -= 1

	if hiddenPos == []:
		print("\n@@@@@@@@@@@@@@@@@@@")
		print("@@@ You've Won! @@@")
		print("@@@@@@@@@@@@@@@@@@@\n")
	else:
		print("\n@@@@@@@@@@@@@@@@@@@@")
		print("@@@ You've lost! @@@")
		print("@@@@@@@@@@@@@@@@@@@@\n")
