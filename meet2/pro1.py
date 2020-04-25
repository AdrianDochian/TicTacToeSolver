#!/usr/bin/pyton3

from helpers import isNumber

name = input("Introdu-ți numele: ")

text = input("Introdu un șir: ")

if isNumber(text):
	print("Sirul de numere a fost gasit de {}".format(name))
else:
	print("Sirul de caractere a fost gasit de {}".format(name))
