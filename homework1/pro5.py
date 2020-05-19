#!/usr/bin/pyton3

from helpers import isNumber

while True:
	print("\n1 – Afisare lista de cumparaturi", 
		"2 – Adaugare element",   
		"3 – Stergere element", 
		"4 – Sterere lista de cumparaturi",  
		"5 - Cautare in lista de cumparaturi\n", sep='\n')
	
	choice = input("\nIntrodu optiunea: ")
	
	if not isNumber(choice):
		print("\nAlegerea nu exista. Reincercati")
	
	else:
		choice = int(choice)
		
		if choice == 1:
			print("\nAfisare lista de cumparaturi")
		
		elif choice == 2:
			print("\nAdugare element")
		
		elif choice == 3:
			print("\nStergere element")
		
		elif choice == 4:
			print("\nSterere lista de cumparaturi")
		
		elif choice == 5:
			print("\nAdaugare element")

		else:
			print("\nAlegerea nu exista. Reincercati")
