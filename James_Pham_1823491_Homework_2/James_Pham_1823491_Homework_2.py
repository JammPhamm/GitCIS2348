def get_month_as_int(monthString):
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input()

if __name__ == '__main__':
    cont = []
    while user_string != '-1':
        cont.append(user_string)
        user_string = input()

    cont2 = []
    for i in cont:
        if len(i.split()) > 1:
            if ',' in i.split()[1]:
                print('{}/{}/{}'.format(get_month_as_int(i.split()[0]), i.split()[1][:-1], i.split()[2]))