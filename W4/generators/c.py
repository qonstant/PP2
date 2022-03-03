number = int(input())
def divisible(n):
    for i in range(12, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
arr = divisible(number)
for i in arr:
    print(i)