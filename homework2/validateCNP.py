#!/bin/python3

# S AA LL ZZ JJ NNN C

months = [666, 31, 666, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
	if year % 4 == 0:
		
		if year % 100 != 0:
			return True

		if year % 400 == 0:
			return True
	else:
		return False

def getYear(S, AA):
	# check 1800-1899
	if S == 3 or S == 4:
		return 1800 + int(AA)

	# check 2000-2099
	if S == 5 or S == 6:
		return 2000 + int(AA)

	# else 1900-2000
	return 1900 + int(AA)

def isDayValid(ZZ, LL, year):
	
	# check for february
	if LL == 2:
		# check for leap year
		if isLeapYear(year):
			
			# leap year february number of days
			if ZZ > 29:
				print("Day in february out of bounds")
				return False
			else:
				return True
		else:

			# normal number of days in february
			if ZZ > 28:
				print("Day in february out of bounds")
				return False
			else:
				return True
	else:

		# check if the day fits
		if ZZ > months[LL]:
			print("Day out of bounds")
			return False
		else:
			return True

def validateCNP(cnp):
	
	# verify length
	if len(cnp) != 13:
		print("Invalid length")
		return False

	# verify if it contains only numbers
	if not cnp.isdigit():
		print("CNP must contain only digits")
		return False

	# tokenize the cnp
	S = int(cnp[0])
	AA = int(cnp[1:3])
	LL = int(cnp[3:5])
	ZZ = int(cnp[5:7])
	JJ = int(cnp[7:9])
	NNN = int(cnp[9:12])
	C = int(cnp[12])

	# verify sex (S)
	if S == 0:
		print("Invalid sex input (S)")
		return False

	# verify month (LL)
	if LL < 1 or LL > 12:
		print("Invalid month input (LL)")
		return False

	# verify day (ZZ)
	if isDayValid(ZZ, LL, getYear(S, AA)) == False:
		return False

	# verify county
	if not ((JJ >= 1 and JJ <= 46) or JJ == 51 or JJ == 52):
		print("Invalid county input (JJ)")
		return False

	# verify sub-county location code
	if NNN == 0:
		print("Invalid sub-county location code (NNN)")
		return False

	# calculate checksum
	generator = "279146358279"
	checksum = 0
	for i in range(0, 12):
		checksum += int(generator[i]) * int(cnp[i])

	checksum %= 11;

	if checksum == 10:
		checksum = 1

	# verify checksum
	if checksum != C:
		print("Invalid checksum (C)")
		return False

	return True
	
while True:
	cnp = input("Enter your CNP: ")
	
	if validateCNP(cnp):
		print (f"CNP: {cnp}  is valid!\n")
	else:	
		print(f"CNP: {cnp} isn't valid!\n")
