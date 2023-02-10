current_month=input('Enter the current month: ')
current_day=input('Enter the current day: ')
current_year=input('Enter the current year: ')
birth_month=input('Enter your birth month: ')
birth_day=input('Enter your birth day: ')
birth_year=input('Enter your birth year: ')

print('Birthday Calculator')
print('Current day:')
print('Month: ', current_month)
print('Day: ', current_day)
print('Year: ', current_year)
print('Birthday')
print('Month: ', birth_month)
print('Day: ', birth_day)
print('Year:    ', birth_year)

if current_month == birth_month and current_day == birth_day:
    print('Happy birthday!')