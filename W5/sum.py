import re
f = open('raw.data', 'r', encoding='utf8')
x = f.read()
pattern = r'Стоимость\n(?P<price>[1-9]{1,3} \d{3}|[1-9]{1,3}\d{0,3})'
prices = re.findall(pattern, x)
prices = [price.replace(' ','') for price in prices]
print(sum(list(map(int, prices))))