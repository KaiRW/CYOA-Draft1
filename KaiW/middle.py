# def middle(x,y,z):
# 	nums = [x,y,z]
# 	list.sort(nums)
# 	return nums.pop(1)

# print(middle(4,53,799))

# def cow(moo,grass,milk):
# 	if moo>=grass and grass>=milk:
# 		return grass
# 	if moo>=milk and milk>=grass:
# 		return milk
# 	if milk>=grass and grass>=moo:
# 		return grass
# 	if milk>=moo and moo>=grass:
# 		return moo
# 	if grass>=milk and milk>=moo:
# 		return milk
# 	if grass>=moo and moo>=milk:
# 		return moo


# print(cow(344,623,5))

# def us(josh,kai_w,kai_bp):
# 	return (josh+kai_w+kai_bp)-min(josh,kai_w,kai_bp)-max(josh,kai_w,kai_bp)

# print(us(10983,3,53))

import random

class Custene:
	def __init__(self,name,phrase,att,defe,hp,spd,attpow):
		self.name= name
		self.att = att
		self.phrase= phrase
		self.defe= defe
		self.hp= hp
		self.spd = spd
		self.attpow =attpow

def dam_value(attacker,defender):
	return (defender.hp-((attacker.attpow*attacker.att)//defender.defe)),((attacker.attpow*attacker.att)//defender.defe)

# def autocombat(X,Y):
# 	if X.spd>Y.spd:
# 		first = X
# 		second = Y
# 	if Y.spd>X.spd:
# 		first = Y
# 		second = X
# 	print("I'm " + first.name + " " + first.phrase)
# 	print("I'm " + second.name + " " + second.phrase)
# 	while first.hp>= 1 and second.hp>=1:
# 		print(first.name+" delt " + str(dam_value(first, second)[1]) + " damage to " + second.name)
# 		second.hp-=(dam_value(first, second)[1])
# 		print(second.name+" has "+str(second.hp)+" left.")
# 		print(second.name + " delt " + str(dam_value(second, first)[1]) + " damage to " + first.name)
# 		first.hp -= (dam_value(second, first)[1])
# 		print(first.name + " has " + str(first.hp) + " left.")
# 	if second.hp<=0:
# 		print (second.name+" is defeated")
# 	if first.hp<=0:
# 		print (first.name+" is defeated")
#
#
#
# enemy= Custene("Josh","and I didn't want the pizza",5,5,20,5,3)
# hero= Custene("Kai teh Bippo","and I would rather be playing video games",5,5,20,4,5)
#
# fight= autocombat(hero,enemy)
#
# thang= Custene("Blip Blop","I'm gonna murder your family after I kill you!",9,400,5,20,4)
# thung= Custene("Fschin Cships","I am your son",4,9,200,5,5)
#
# fit= autocombat(thung,thang)

def combat(Pc,Cp):
	if Cp.spd>Pc.spd:
		print("I'm " + Cp.name + " " + Cp.phrase)
		print("I'm " + Pc.name + " " + Pc.phrase)
		print(Cp.name+" delt " + str(dam_value(Cp, Pc)[1]) + " damage to " + Pc.name)
		Pc.hp-=(dam_value(Cp, Pc)[1])
		print(Pc.name + " has " + str(Pc.hp) + " left.")
	if Pc.spd>Cp.spd:
		print("I'm " + Pc.name + " " + Pc.phrase)
		print("I'm " + Cp.name + " " + Cp.phrase)

enemy= Custene("Josh","and I didn't want the pizza",5,5,20,5,3)
hero= Custene("Kai teh Bippo","and I would rather be playing video games",5,5,20,4,5)

fight= combat(hero,enemy)