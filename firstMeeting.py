#!/usr/bin/python3

for x in range(2, 100):
	i = 2
	flag = 1
	while i <= (x / 2):
		if x % i == 0:
			flag = 0
		i += 1
	if flag == 1:
		print("%d e prim", x)