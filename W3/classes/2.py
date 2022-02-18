class Shape():
    def __init__(self):
        pass
    def print_area(self):
        print(0)
class Square(Shape):
    def __init__(self, length = 0):
        super(Square, self).__init__()
        self.length = length
    def print_area(self):
        self.area = int(self.length) ** 2
        print(self.area)
Sqr = Square(int(input("Enter the length of the square: ")))
Shp = Shape()
print('Area of the square is: ', end ='')
# Area of the square
Sqr.print_area()
# The default area of the shape
print('Default area of the shape is: ', end ='')
Shp.print_area() 
