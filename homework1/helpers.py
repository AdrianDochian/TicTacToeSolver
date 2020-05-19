#!/usr/bin/pyton3

def isNumber(text):
	for atom in text:
		if atom < '0' or atom > '9':
			return False
	return True
