numbers = int(input())

def square(n):
    for i in range(n+1):
        yield i**2
print(*square(numbers))