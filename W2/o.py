x, y = map(str, input().split('+'))
dictn = {'ZER': 0, 'ONE': 1, 'TWO': 2,
        'THR': 3, 'FOU': 4, 'FIV': 5,
        'SIX': 6, 'SEV': 7, 'EIG': 8,
        'NIN': 9}
dictst = {0: 'ZER', 1: 'ONE', 2: 'TWO',
         3: 'THR', 4: 'FOU', 5: 'FIV',
         6: 'SIX', 7: 'SEV', 8: 'EIG',
         9: 'NIN'}
fst = []
scnd = []
j=0
for i in range(3, len(x)+1, 3):
    fst.append(x[j: i])
    j+=3
j=0
for i in range(3, len(y)+1, 3):
    scnd.append(y[j: i])
    j+=3
num1 = 0
num2 = 0
for i in fst:
    num1 = num1*10 + dictn[i]
for i in scnd:
    num2 = num2*10 + dictn[i]
num1 = num1 + num2
num1 = str(num1)
for i in num1:
    a = int(i)
    print(dictst[a], end = '')