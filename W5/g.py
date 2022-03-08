import re
def jylan_to_tuie(text):
    arr = text.split('_')
    arr = [x.capitalize() for x in arr]
    arr[0] = arr[0].lower()
    text = ''.join(arr)
    return text
print(jylan_to_tuie('snake_to_camel'))
