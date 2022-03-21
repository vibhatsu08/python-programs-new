#python program to calculate the area of a circle.
from cmath import pi


area = 0
radius = int(input("Enter the radius of a circle: "))

area = pi * radius ** 2
print(area)