number = int(input())
def rnums(n):
    for i in range(n, 0, -1):
        yield i
arr = rnums(number)
for i in arr:
    print(i)
        