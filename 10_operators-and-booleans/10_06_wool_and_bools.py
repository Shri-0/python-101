# Write a code snippet that gives a name to a `sheep`
# and uses a boolean value to define whether it has `wool` or not.


sheep_name = input("Please write the name of the sheep ")

wool_or_not = input("Does " + sheep_name + " Have any wool? ")
#wool_or_not = False
#wool_or_not.lower()

#while wool_or_not != False:
if wool_or_not.lower() == "no":
	print("It does not have wool ")
	print(False)

elif wool_or_not.lower() == "yes":
	print("Yes it has wool!")
	print(True)
else:
    print("try again")
