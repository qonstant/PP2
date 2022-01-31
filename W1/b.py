def isTasty(s, n):
    if(n > 0):
        return (ord(s[n-1]) + isTasty(s, n - 1))
    else:
        return 0

s = str(input())
n, sum = len(s), 0
res = isTasty(s, n)
if(res > 300):
    print("It is tasty!")
else:
    print("Oh, no!")