class Shape():
    def __init__(self):
        pass
    def print_area(self):
        print(0)
class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
    def print_area(self):
        self.area = int(self.length) ** 2
        print(self.area)