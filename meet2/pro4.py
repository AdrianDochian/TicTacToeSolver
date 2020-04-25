#!/usr/bin/pyton3

number = int(input("Introdu un număr: "))

if number > 0: 
	if number < 10:
		print("Numărul este pozitiv și mai mic decât 10".format(number))

elif number < 0:
	print(abs(number))

else:
	print("Numarul este 0")