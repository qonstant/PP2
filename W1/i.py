a = []
cnt = 0
n = int(input())
for i in range(n):
    s = input()
    if(s.endswith('@gmail.com') == True):
        a.append(s.replace('@gmail.com', ''))
        
for i in range(len(a)):
    print(a[i])