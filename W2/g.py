n = int(input())
dem = {}
hun = {}
for i in range(n):
    name, k = input().split()
    if k in dem:
        dem[k] += 1
    elif not k in dem:
        dem[k] = 1
m = int(input())
for i in range(m):
    name, k, times = input().split()
    if k in hun:
        hun[k] += int(times)
    elif not k in hun:
        hun[k] = int(times)
sum = 0
for k in dem:
    if not k in hun:
        sum += dem[k]
    elif dem[k] - hun[k] >= 0 and k in hun:
        sum += dem[k] - hun[k]
print('Demons left: ' + str(sum))