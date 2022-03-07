import re
def spaces(text):
    pattern = r'[A-Z]{1}[a-z]*'
    arr = re.findall(pattern, text)
    text = ' '.join(arr)
    return text
text = 'WordsStrungTogether'
print(spaces(text))