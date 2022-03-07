import re
def find(text):
    pattern = r'a{1}.*b$'
    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'
print(find('adfggfdb'))
print(find('dfhkalkjfdFGHF___jdfb'))
print(find('DFHKJsdadfgj_lkk_bg'))
print(find('DFHKJsdadfgj_lkk_b'))
