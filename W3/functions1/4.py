def is_prime(num):
    result = True
    for i in range(2, num//2):
        if num % i == 0:
            result = False
            break
    return result
def filter_prime(*args):
    l = []
    for i in args:
        if is_prime(i) == True:
            l.append(i)
    return l
lst = list(map(int, input().split()))
print(*filter_prime(*lst), end = ' ')