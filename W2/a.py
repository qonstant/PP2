s = list(map(int,input().split()))
jmps = 0
for i in range(len(s)):
    if jmps >= len(s)-1:
        print(1)
        exit()
    if jmps < i:
        print(0)
        exit()
    if jmps < s[i] + i:
        jmps = s[i] + i