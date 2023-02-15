import math

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')
print('Paint needed:', '{:.2f}'.format(wall_area / 350), 'gallons')
print('Cans needed:', math.ceil(wall_area / 350), 'can(s)')
print()
paint_color = input('Choose a color to paint the wall:\n')
price = 0

if paint_color == 'red':
    price = 35
elif paint_color == 'blue':
    price = 25
elif paint_color == 'green':
    price = 23
else:
    print('Invalid color! Pick "red", "green" or "blue"!')

print(f'Cost of purchasing', paint_color, 'paint:', '${}'.format(price*(math.ceil(wall_area / 350))))
