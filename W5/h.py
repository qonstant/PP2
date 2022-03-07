import re
text = "PythonTutorialAndExercises"
pattern = r'[A-Z]{1}[a-z]*'
print(*re.findall(pattern, text), end = ' ')
