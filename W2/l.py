def brack(s):
    if '()' in s or '[]' in s or '{}' in s:
        return True
    else:
        return False
s = input()
while brack(s)==True:
    if '()' in s:
        s = s.replace('()', '')
    if '[]' in s:
        s = s.replace('[]', '')
    if '{}' in s:
        s = s.replace('{}', '')
print('Yes' if len(s)==0 else 'No')