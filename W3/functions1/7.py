def has_33(*nums):
    starr = [str(x) for x in nums]
    string = ''.join(starr)
    if '33' in string:
        return True
    else:
        return False
print(has_33(*(list(map(str, input().split(' '))))))