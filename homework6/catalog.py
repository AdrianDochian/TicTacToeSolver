class Catalogue():
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
		self.absences = 0
		self.courses = {}

	def __str__(self):
		return f"{self.firstName} {self.lastName} has {self.absences} absences!"

	def hasAbsented(self):
		self.absences += 1


	def discardAbsences(self, nrOfAbsencesToDiscard):
		if str(nrOfAbsencesToDiscard).isdigit():
			nrOfAbsencesToDiscard = int(nrOfAbsencesToDiscard)
			
			if nrOfAbsencesToDiscard > self.absences:
				self.absences = 0
			else:
				self.absences -= nrOfAbsencesToDiscard

		else:
			print("Invalid input at discarding absences!")

class CatalogueUpgraded(Catalogue):
	def __init__(self, firstName, lastName):
		super().__init__(firstName, lastName)

	def updateCatalogue(self, course, value):
		self.courses.setdefault(course, value)
	
	def showCourses(self):
		print(f"For {self.firstName} {self.lastName}:")

		for key in self.courses.keys():
			print(key)

	def showMeanGrades(self):
		print(f"For {self.firstName} {self.lastName}:")
		for key in self.courses.keys():
			
			finalGrade = 0
			gradesCounter = 0

			for nota in self.courses.get(key):
				
				if str(nota).isdigit():
					finalGrade += int(nota)
					gradesCounter += 1


			finalGrade /= gradesCounter 
			print(f"{key} -> {finalGrade}")

student1 = CatalogueUpgraded("Ion", "Roata")
student1.hasAbsented()
student1.hasAbsented()
student1.hasAbsented()
student1.discardAbsences(2)

student2 = CatalogueUpgraded("George", "Cerc")
student2.hasAbsented()
student2.hasAbsented()
student2.hasAbsented()
student2.hasAbsented()
student2.discardAbsences(2)

print(student1, student2, sep='\n')

student1.updateCatalogue("Python", [6, 7, 8])
student2.updateCatalogue("Python", [8, 9, 10])
student2.updateCatalogue("Matematica", [8, 9, 10])
student1.updateCatalogue("Romana", [6, 7, 8])

student1.showCourses()
student2.showCourses()

student1.showMeanGrades()
student2.showMeanGrades()
