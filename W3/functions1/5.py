from itertools import permutations
def nextperm(n):
    arr = permutations(n)
    for i in list(arr): 
        print(*i, sep='')
nextperm(input())