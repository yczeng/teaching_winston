'''
Goal:
We're going to have a cat party.
5 different cats: Bob, Joe, Susan, Jack, Zack
We create an object called cat
'''

'''
Cat object
input: name - String, age - Integer, species - string, hobbies - string, friendly_meter - Integer
'''
class Cat:
	def __init__(self, name, age, species, hobbies, happy_meter, favorite_food):
		self.name = name
		self.age = age
		self.type = species
		self.hobbies = hobbies
		self.happy_meter = happy_meter
		self.favorite_food = favorite_food

	def printNames(self):
		print("This cat's name is: ", self.name)

	'''
	needYarn figures out whether or not we need yarn depending on the cat's hobbies
	returns True or False
	'''
	def needYarn(self):
		if self.hobbies == "playing with yarn":
			return True
		else:
			return False

	'''
	if the cat's friendly is > 5 is friendly, then it will purr. Otherwise it will growl.
	'''
	def response(self):
		if self.happy_meter > 5:
			return "purr"
		else:
			return "hiss"

	def health(self):
		if self.hobbies == "nothing" and happy_meter < 5:
			return "sick"
		else:
			return "okay"

cat1 = Cat("Bob", 5, "Tabby", "playing with yarn", 7, "cornflakes")
cat2 = Cat("Joe", 8, "Siamese", "play with rubber ball", 6, "cornflakes")
cat3 = Cat("Susan", 18, "Albecenian", "sleep", 4, "milk")
cat4 = Cat("Jack", 2, "Tabby", "Chase butterflies", 9, "butterflies")
cat5 = Cat("Zack", 2, "Tabby", "Chase butterflies", 8, "butterflies")
cat6 = Cat("Willy", 18, "Albecenian", "sleep", 4, "milk")

cats = [cat1, cat2, cat3, cat4, cat5, cat6]

# for eachCat in cats:
# 	eachCat.printNames()

'''
takes in an array of cat objects and returns an array of array of friend group

sampleinput: [cat1, cat2, cat3, cat4, cat5]
sampleoutput: {"cornflakes": [cat1, cat2], "butterflies": [cat4, cat5], "milk": [cat3, cat6]}

'''
def catFriends(cats_array):
	food_friend_group = {}
	for eachCat in cats:
		if eachCat.favorite_food not in food_friend_group:
			food_friend_group[eachCat.favorite_food] = [eachCat.name]
		else:
			food_friend_group[eachCat.favorite_food].append(eachCat.name)
	return food_friend_group

print(catFriends(cats))


# =================== old code ===========================
# print(cat1.name)
# print(cat1.age)
# cat1.printNames()
# print("Does the cat need yarn?", cat1.needYarn())
# print(cat1.response())
# print(cat1.health())