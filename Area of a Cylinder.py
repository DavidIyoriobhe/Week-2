#This program is to calculate the Area of a Cylinder
from math import pi
radius = float(input("Enter a value for radius: "))
height = float(input("Enter a value for heigh: "))
Area = (2*pi*radius**2)+height*(2*pi*radius)
print("Area of the Cylinder is ", round(Area,4))
