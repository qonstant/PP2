s = input()
x = input()
if(s.find(x) != s.rfind(x)):
    print(s.find(x), s.rfind(x), sep = " ")
else:
    print(int(s.find(x)))