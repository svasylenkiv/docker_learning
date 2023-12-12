import calendar

print('welcome to the calendar\n')

year = int(input('Please enter year: '))
month = int(input('Enter any month number: '))

print(calendar.month(year, month))

print('Best wishes!')