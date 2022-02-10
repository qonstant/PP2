n = int(input())
ans = []
for i in range(n):
    s = input()
    up = False
    low = False
    num = False
    for j in s:
        if j.isupper():
            up = True
        if j.islower():
            low = True
        if j.isdigit():
            num = True
        if num == True and low == True and up == True:
            if not s in ans:
                ans.append(s)
            break
ans.sort()
print(len(ans), *ans, sep = '\n')     