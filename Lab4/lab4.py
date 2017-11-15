class Animal(object):
	def __init__(self,sound,name,age,favourite_colour):
		self.sound = sound
		self.name = name
		self.age = age
		self.favourite_colour = favourite_colour
	def make_sound(self,times):
		print(self.name + ": " + (self.sound*times) + "pickachu!")

pikachu = Animal("pika! ", "Pikachu", "12", "Yellow")
pikachu.make_sound(200)

class Person(object):
	def __init__(self,name,age,city,gender,breakfast):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.breakfast = breakfast
	def eat(self):
		print("Hey my name is " + self.name + " and I loooooove eating " + self.breakfast)
	def visit(self, when):
		print("I would like to visit " + self.city + " " + when + "!")
Idan = Person("Idan","16","Hannover","male","a cookie")
Idan.eat()
Idan.visit("in april")

class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def Sing(self):
		for value in self.lyrics:
			print(value)
all_star = Song(["Somebody once told me","the world is gonna roll me","I ain't the sharpest tool in the shed","she was looking kind of dumb","with her finger and her thumb","in the shape of an L on her forehead"])
all_star.Sing()
