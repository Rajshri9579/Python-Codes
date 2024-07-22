#Function returning multiple values
#Create a function that returns both the area and circumference of a circle given is radius.

import math
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a,c = circle_stats(4)
print("Area: ",a, "Circumference: ",c )