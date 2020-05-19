#!/usr/bin/pyton3

year = int(input("Introdu un an: "))

if year % 4 == 0: 
	print("Anul {} este bisect".format(year))
else:
	print("Anul {} nu este bisect".format(year))
