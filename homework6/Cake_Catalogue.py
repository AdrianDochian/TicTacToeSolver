def getPrice(triple):
	return triple[1]

def getWeight(triple):
	return triple[2]

class Cake_Catalogue:
	cakes = []

	def __init__(self, name, price, weight):
		self.name = name
		self.price = price
		self.weight = weight
		self.cakes.append((name, price, weight))

	def printByPrice(self):
		print("Ordering by price:")
		self.cakes.sort(key = getPrice)

		for triple in self.cakes:
			print(f"{triple[0]} -> costing {triple[1]}$ and weighting {triple[2]}KG")

	def printByWeight(self):
		print("Ordering by weight:")
		self.cakes.sort(key = getWeight)

		for triple in self.cakes:
			print(f"{triple[0]} -> costing {triple[1]}$ weighting {triple[2]}KG")

	def __str__(self):
		return "{} -> ({}, {})".format(self.name, self.price, self.weight)

class Cake(Cake_Catalogue):
	def setInfo(self, leveled = False, glaze = "Chocolate"):
		self.leveled = leveled
		self.glaze = glaze

	def getInfo(self):
		return "{} -> leveled = {} | glaze = {}".format(self.name, self.leveled, self.glaze)

class Cookie(Cake_Catalogue):
	pass

cake1 = Cake("cake1", 10, 30)


cake2 = Cake("cake2", 20, 40)
cake3 = Cake("cake3", 30, 50)

cookie1 = Cookie("cookie1", 10, 30)
cookie2 = Cookie("cookie2", 20, 40)
cookie3 = Cookie("cookie3", 30, 50)

cake1.printByWeight()
cake1.printByPrice()

cake1.setInfo(True, "Cocoa")

print(cake1.getInfo())

cake2.setInfo()
print(cake2.getInfo())