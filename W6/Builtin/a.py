def multiplyList(*arr):
    res = 1
    for i in arr:
        res *= i
    return res
arr = list(map(int, input('Enter the array:\n').split()))
print(multiplyList(*arr))