import math
def isPrime(number):
    for i in range(2, number//2):
        if number % i == 0:
            return False
    else:
        return True
nums = list(map(int, input().split()))
max = max(nums)
for i in nums:
    for j in range(2, i//2): 
        nums = filter(lambda x: isPrime(x) == True, nums)
print(*nums)