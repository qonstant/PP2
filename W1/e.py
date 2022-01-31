x, y = map(int, input().split())
isPrime = True
max = int(x / 2 - 1)
for i in range(2, max):
    if(x % i == 0 or i > x):
        isPrime = False
        break
if(isPrime == True and x < 500 and y % 2 == 0):
    print('Good job!')
else:
    print('Try next time!')