import re
def find(text):
        patterns = r'ab{2,3}'
        if re.search(patterns,  text):
                return 'Yes'
        else:
                return('No')
print(find('ab'))
print(find('ba'))
print(find('abbb'))
print(find('abc'))