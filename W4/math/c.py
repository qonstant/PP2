import math
number = int(input('Input number of sides: '))
length = int(input('Input the length of a side: '))
area = (number*pow(length,2))/(4*math.tan(math.radians(180/number)))
print(f'The area of the polygon is: {int(area)}')