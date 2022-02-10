n = int(input())
for i in range(n):
    for j in range(n):
        if n%2 == 0:
            if j <= i:
                print('#', end='')
            elif j > i:
                print('.', end='')
        else:
            if i >= n - j - 1:
                print('#', end='')
            else:
                print('.', end='')
    print()