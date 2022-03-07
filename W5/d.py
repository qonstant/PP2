import re
def find(text):
    pattern = r'[A-Z]{1}_[a-z]+'
    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'
print(find('a_b'))
print(find('A_casdasd'))
print(find('AASD_asda'))
print(find('F_asd'))