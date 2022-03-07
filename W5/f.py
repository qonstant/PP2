import re
text = 'Write a Python program to replace all occurrences of space, comma, or dot with a colon.'
text = re.sub('[\s.,]', ':', text)
print(text)