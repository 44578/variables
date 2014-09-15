#john bain
#variable improvement exercise
#05-09-12
import math
Radius = float(input("please enter the radius of the circle: "))

Circumference = 2* math.pi * Radius
Circumference = round(Circumference,2)

Area = math.pi * Radius**2
Area = round(Area,2)

print("The circumference of this circle is {0}.".format(Circumference))
print("The area of this circle is {0}.".format(Area)) 
