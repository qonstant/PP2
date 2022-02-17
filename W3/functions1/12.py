def histogram(*arg):
    for i in arg:
        for j in range(i):
            print('*', end = '')
        print()
arr = list(map(int, input().split()))
histogram(*arr)