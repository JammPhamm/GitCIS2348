#James Pham, 1823491
# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]

while name != '-1':
    # Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1

        # printing name and age
        print('{} {}'.format(name, age))

    except ValueError:

        # printing name and age as 0
        print('{} {}'.format(name, 0))

    # Get next line
    parts = input().split()
    name = parts[0]