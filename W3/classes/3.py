from secondtsc import Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def print_area(self):
        self.area  = self.length * self.width
        print(self.area)
Rec = Rectangle(int(input('Enter the length of the rectangle: ')), int(input('Enter the width of the rectangle: ')))
print('Area of the rectangle is: ', end = '')
Rec.print_area()