age = 23

if age >=18:
    print("You are adult and you can buy alcohol")
else:
    print("you are too young to buy alcohol")

isDrunk= True
if age >=18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("you are too young to buy alcohol")

isRestrictedArea =False

if age >=18 and not isDrunk and not isRestrictedArea:
    print("You are adult and you can buy alcohol")
else:
    print("you are too young to buy alcohol")

