arr = []
while True:
    a = int(input())
    if a != 0:
        arr.append(a)
    else:
        break
if len(arr)%2 == 0:
    l = len(arr)//2
else:
    l = len(arr)//2 + 1
for i in range(l):
    if i == l - 1 and len(arr)%2 != 0:
        print(arr[i])
    else:
        print(arr[i] + arr[-i-1], end = ' ')