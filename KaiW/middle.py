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

class bobstats():
	att = 7
	defe= 9
	hp=80
	attpow= 2

class blobstats():
	att= 2
	defe=4
	hp=22
	attpow=3

def dam_value(attacker,defender):
	return (defender.hp-((attacker.attpow*attacker.att)//defender.defe)),((attacker.attpow*attacker.att)//defender.defe)

print("delt "+str(dam_value(bobstats,blobstats)[1])+" damage")

