# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

int1 = 3
int1 = float(int1)

float2 = 5.0
float2 = int(float2)

int2 = 6
float1 = 2.5

Division = int2 / float1
Mult = int2 * float1

print(int1)
print(float2)
print(Division)
print(int(Mult))

# The information for int2 is lost due to the fact that the conversion comes out to floating points, unless you convert it back to an integer
