# import random
# health = 100
# items = []
# print (items)
# print("health = " + str(health))
# print("You walk into a forest")

# answer = input("A wild boar appears what will you do:\nA)Run\nB)Climb A Tree\nC)Fight With A Stick\nD)Hide And Hope It Doesn't Notice You\n\nPress I for items")
# 	if answer == "A" or "a":
# 	print("You Try To Run")
# 	chance = random.randrange(1, 10)
# 	if chance <= 3:
# 		print("You Escape")
# 	else:	
# 		print("You Fail And The Boar Charges Into You")
# 		health -= 10
# 		print("health = " + str(health))
# 	elif answer == "B" or "b":
# 		print("You Try To Climb The Tree But Fail")
# 	elif answer == "C" or "c":
# 		print("You Try To Fight It With A Stick")
# 	elif answer == "D" or "d":
# 		print("You Try To Hide")
# 	elif answer == "I" or "i":
# 		print(items)`
# 			play()

# play()


# q = "do you like cheese: A) Yes B) No C) Maybe D) So"
# o = ["yes","no","maybe","so"]

# def play(question,option):
# 	answer = input(question)
# 	if answer == "A" or "a":
# 		return options[0]
# play(q,o)

# def  add(x,y):
# 	return x + y
# def subtract(x,y):
# 	return x - y
# def multiply(x,y):
# 	return x * y
# def divide(x,y):
# 	return x / y
# def calc(function,x,y):
# 	return function(x,y)
# print(calc(add,1,2))

# number = 4

# def thing():
# 	global number
# 	number = number + 1
# 	return number ** 2
# print(thing())

import random
gameon = True
health = 100
for i in range(50):
	print()

class Question():
	def __init__(self,question,choices):
		self.question=question
	def get_question(self):
		return self.question

def probability(prob):
	def chance():
		if random.randint(1,100) <= prob:
			return True
		else:
			return False
		return chance

query= Question("You wake up in a forest, you spot a boar running towards you, do you: \nA)run, \nB)fight")
print(query.get_question())




# the higher the probability the greater chance of success

# def rand_function(gain,loss,fail,succeed,probability):
# 	global health
# 	if random.randint(1,100) <= probability:
# 		health+= gain
# 		print(succeed)
# 		return questionrunboarw
# 	else:
# 		health-= loss
# 		print(fail)
# 		return questionrunboarl

# questionrunboarw= ["You escape from the boar. You find a river, do you: \n A)follow the river upstream, \n B)follow the river downstream \n C)cross the river",{"a":"Option1","b":"Option2","c":"Option3"}]
# questionrunboarl=["You fail to escape from the boar"]
# question1= ["You wake up in a forest, you spot a boar running towards you, do you: \nA)run, \nB)climb a tree, \nC)attack the boar with a tree branch, \nD)stay still and hope it doesn't notice you",{"a": rand_function(0, 10,"You successfully escape the boar","You failed to outrun the boar, you lose ten health", 70),"b":"questionclimb","c":"Option3","d":"Option4"}]

# question = question1

# while gameon:
# 	answer = input(question[0])
# 	question = question[1][answer]
# 	print("\nHealth =" + str(health))
# 	print()
		
# Thegame = []
# Thegame.append("cow")