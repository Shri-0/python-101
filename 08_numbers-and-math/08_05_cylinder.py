# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

Pi = 3.14
Height = 5
Radius = 3.14

CylVolume = float(Pi * (3.14 ** 2) * Height)
SurfaceArea = float(((3.14 * 2) * Radius * Height) + ((2 * Pi) * (Radius ** 2)))

print("The Volume of the cylinder is " + str(CylVolume))
print("The Surface Area of the Cylinder is " + str(SurfaceArea))
