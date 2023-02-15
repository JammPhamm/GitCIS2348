Services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

print("Davy's auto shop services")
print('Oil change --', '${}'.format(Services.get('Oil change')))
print('Tire rotation --', '${}'.format(Services.get('Tire rotation')))
print('Car wash --', '${}'.format(Services.get('Car wash')))
print('Car wax --', '${}'.format(Services.get('Car wax')))
print()
first_service = input('Select first service:\n')
second_service = input('Select second service:\n')
print()
print("Davy's auto shop invoice")
print()
if first_service == '-':
    print('Service 1: No service')
else:
    print('Service 1: {},'.format(first_service), '${}'.format(Services.get(first_service)))

if second_service == '-':
    print('Service 2: No service')
else:
    print('Service 2: {},'.format(second_service), '${}'.format(Services.get(second_service)))

print()
total = int(Services.get(first_service) + Services.get(second_service))
print('Total:', '${}'.format(total))
