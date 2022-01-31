n = int(input())
a = []
for i in range(0, n):
    a.append(input())
for i in a:
    if(int(i) <= 10):
        print("Go to work!", end="\n")
    elif(10 < int(i) <= 25):
        print("You are weak", end="\n")
    elif(25 < int(i) <= 45):
        print("Okay, fine", end="\n")
    elif(45 < int(i)):
        print("Burn! Burn! Burn Young!", end="\n")