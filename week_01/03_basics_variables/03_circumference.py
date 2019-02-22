'''
Write the necessary code that prints out the area and circumference
of a circle with a radius of 3.14

'''

from math import pi

radius = 4

def area(radius):
    return pi*radius**2

def circumference(radius):
    return pi*radius*2

print(area(radius))
print(circumference(radius))