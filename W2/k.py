st = map(str, input().split())
symbols = ['!', '.', ';', ',', '?']
ans = []
for word in st:
    wrd = []
    for i in word:
        if not i in symbols:
            wrd.append(i)
    s = ''.join(wrd)
    if not s in ans:
        ans.append(s)
ans.sort()
print(len(ans), *ans, sep = '\n')