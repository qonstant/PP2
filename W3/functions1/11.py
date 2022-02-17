def is_palidrome(word):
    rev = ''.join(reversed(word))
    if word == rev:
        return True
    else:
        return False
print(is_palidrome(input()))