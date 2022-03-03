from datetime import datetime, time
from time import strptime
def diff_in_sec(first, second):
    difference = first - second
    print(difference.seconds)
    return difference.days *24*3600 + difference.seconds

date1 = datetime.today()
year = input('Enter any previous or current year:\n')
month = input('Enter the month:\n')
day = input('Enter the day:\n')
hour = input('Enter the hour:\n')
minute = input('Enter the minute:\n')
second = input('Enter the second:\n')
date2 = datetime.strptime(f'{year}/{month}/{day} {hour}:{minute}:{second}', f'%Y/%m/%d %H:%M:%S')
print('Difference in seconds is:', diff_in_sec(date1, date2))