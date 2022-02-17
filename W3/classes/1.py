class Str():
    def __init__(self):
        self.string = ''
    def getString(self):
        self.string = input('Enter the string: \n')
    def printString(self):
        print(self.string.upper())
s = Str()
s.getString()
s.printString()