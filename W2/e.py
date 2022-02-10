ar = list(map(int, input().split()))
if len(ar) == 1:
    ar.append(int(input()))
a = []
n = ar[0]
x = ar[1]
for i in range(int(n)):
    a.append(x + 2*i)
res = a[0]
for i in range(1, n):
    res = res^a[i]
print(res)