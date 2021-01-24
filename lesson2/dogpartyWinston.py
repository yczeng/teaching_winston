'''
we are going to have a dog party
different dogs: Howler, bolt, Ace, summer, snowfall, ciff, 
'''

class Dog:

	def __init__(self, name, age, species, fav_food, happy_meter, hobbies, school):
		self.name = name
		self.age = age
		self.species = species
		self.hobbies = hobbies
		self.happy_meter = happy_meter
		self.fav_food = fav_food
		self.school = school

	def Names_of_Dogs(self):
		print ("This Dogs name is: ", self.name)

	def Hobbie(self):
		return hobbies

	def How_happy(self):
		if self.happy_meter >= 5:
			return "Whine"
		else:
			return "Growl"

	def obedience(self):
		if school == "obedienceschool" and age >= 3 and age <= 6:
			return "You are inrolled!!"
		else:
			return school

	def kind_of_dog(self):
		if self.dog_type == "Siberian Husky":
			return "Husky"
		elif self.dog_type == "Alaskan Malamute":
			return "Malamute"
		elif self.dog_type == "labador retriver":
			return "retriver"

	def health(self):
		if self.hobbies == "nothing" and happy_meter < 3:
			return "not well"
		else:
			return "ok"

dog1 = Dog("Howler", 2, "Siberian Husky", "chewing tennis balls", 10, "Dog kibble", "not yet")
dog2 = Dog("Ace", 4, "labador retriver", "playing fetch", 8, "bananas", "obedienceschool")
dog3 = Dog("Snowfall", 6 ,"Alaskan Malamute", "playing in the snow", 8, "watermelon", "finished")
dog4 = Dog("Bolt", 2, "labador retriver", "chewing tennis balls", 10, "Dog kibble", "not yet")
dog5 = Dog("Ember", 5, "Siberian Husky", "playing in the snow", 9, "watermelon", "finished")
dog6 = Dog("Cliff",4 , "labador retriver", "playing fetch", 8, "bananas", "obedienceschool")

dogs = [dog1, dog2, dog3, dog4, dog5, dog6]

def DogFriends(Dogs_array):
	food_friend_group = {}
	for eachDog in dogs:
		if eachDog.fav_food not in food_friend_group:
			food_friend_group[eachDog.fav_food] = [eachDog.name]
		else:
			food_friend_group[eachDog.fav_food].append(eachDog.name)
	return food_friend_group

print(DogFriends(dogs))

print(dog1.name)
print(dog1.age)
print(dog1.species)
print(dog1.hobbies)
print(dog1.happy_meter)
print(dog1.fav_food)
print(dog1.school)
print(dog1.How_happy())
print(dog1.health())
print(dog2.name)
print(dog2.age)
print(dog2.species)
print(dog2.hobbies)
print(dog2.happy_meter)
print(dog2.fav_food)
print(dog2.school)
print(dog2.How_happy())
print(dog2.health())
print(dog3.name)
print(dog3.age)
print(dog3.species)
print(dog3.hobbies)
print(dog3.happy_meter)
print(dog3.fav_food)
print(dog3.school)
print(dog3.How_happy())
print(dog3.health())
print(dog4.name)
print(dog4.age)
print(dog4.species)
print(dog4.hobbies)
print(dog4.happy_meter)
print(dog4.fav_food)
print(dog4.school)
print(dog4.How_happy())
print(dog4.health())
print(dog5.name)
print(dog5.age)
print(dog5.species)
print(dog5.hobbies)
print(dog5.happy_meter)
print(dog5.fav_food)
print(dog5.school)
print(dog5.How_happy())
print(dog5.health())
print(dog6.name)
print(dog6.age)
print(dog6.species)
print(dog6.hobbies)
print(dog6.happy_meter)
print(dog6.fav_food)
print(dog6.school)
print(dog6.How_happy())
print(dog6.health())
