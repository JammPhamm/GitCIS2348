lemon_amount = int(input('Enter amount of lemon juice (in cups):\n'))
water_amount = int(input('Enter amount of water (in cups):\n'))
agave_nectar_amount = float(input('Enter amount of agave nectar (in cups):\n'))
serving_amount = int(input('How many servings does this make?\n'))

print('Lemonade ingredients - yields', '{:.2f}'.format(serving_amount), 'servings')
print('{:.2f}'.format(lemon_amount), 'cup(s) lemon juice')
print('{:.2f}'.format(water_amount), 'cup(s) water')
print('{:.2f}'.format(agave_nectar_amount), 'cup(s) agave nectar')

desired_serving_amount = int(input('How many servings would you like to make?\n'))

print('Lemonade ingredients - yields', '{:.2f}'.format(desired_serving_amount), 'servings')
print('{:.2f}'.format(lemon_amount*8), 'cup(s) lemon juice')
print('{:.2f}'.format(water_amount*8), 'cup(s) water')
print('{:.2f}'.format(agave_nectar_amount*8), 'cup(s) agave nectar')
