current_month = int(input('Enter the current month: '))
current_day = int(input('Enter the current day: '))
current_year = int(input('Enter the current year: '))
birth_month = int(input('Enter your birth month: '))
birth_day = int(input('Enter your birth day: '))
birth_year = int(input('Enter your birth year: '))
age = current_year - birth_year
if current_month < birth_month:
    age = age - 1

print('Birthday Calculator')
print('Current day:')
print('Month: ', current_month)
print('Day: ', current_day)
print('Year: ', current_year)
print('Birthday:')
print('Month: ', birth_month)
print('Day: ', birth_day)
print('Year:    ', birth_year)
print('You are ', age, 'years old.')

if current_month == birth_month and current_day == birth_day:
    print('Happy birthday!')
