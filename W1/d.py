n = float(input())
z = input()
if(z == 'k'):
    c = int(input())
    print(round((n/1024), c))
else: 
    print(round(n*1024)) 