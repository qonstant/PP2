def isPrime(number):
    for i in range(2, number//2):
        if number % i == 0:
            return False
    else:
        return True
nums = list(map(int, input().split()))
for i in nums:
    nums = filter(lambda x: isPrime(x) == True, nums)
print(*nums)
