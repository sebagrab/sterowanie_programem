age = 23

if age >=18:
    print("You are adult and you can buy alcohol")
else:
    print("you are too young to buy alcohol")

isDrunk= False
if age >=18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("you are too young to buy alcohol")

isRestrictedArea =False

if age >=18 and not isDrunk and not isRestrictedArea:
    print("You are adult and you can buy alcohol")
else:
    print("you are too young to buy alcohol")

if age <18:
    print("too young")
elif isDrunk:
    print("are you drank")
elif isRestrictedArea:
    print("nie wolno tu")
else:
    print("kup se")

print("tak")
print("czy dzila")

to tez
