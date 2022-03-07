import re
def find(text):
    pattern = r'^[a-z]+_[a-z]+$'
    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'
print(find('a_b'))
print(find('ab'))
print(find('aa_sdv'))
print(find('asasd_'))