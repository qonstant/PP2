import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(f'Today is {today}')
print(f'Yesterday is {yesterday}')
print(f'Tomorrow is {tomorrow}')