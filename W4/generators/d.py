begin, end = map(int, input().split())
def squares(a, b):
    for i in range(a, b+1):
        yield i**2 
arr = squares(begin, end)
for i in arr:
    print(i)