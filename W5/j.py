import re
def tuie_to_jylan(text):
    pattern = r'[A-Z]+[a-z]*'
    arr = re.findall(pattern, text)
    arr = [x.lower() for x in arr]
    text = '_'.join(arr)
    return text
text = 'TuieCaseHelloWorld'
print(tuie_to_jylan(text))