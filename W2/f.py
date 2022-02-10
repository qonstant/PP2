n = int(input())
dict = {}
for i in range(n):
    name, money = input().split()
    if name in dict:
        dict[name] += int(money)
    elif not name in dict:
        dict[name] = int(money)
maxim = max(i for i in dict.values())
for k in sorted(dict.keys()):
    if dict[k] == maxim:
        print(k + ' is lucky!')
    else:
        print(k + ' has to receive ' + str(maxim - dict[k]) + ' tenge')