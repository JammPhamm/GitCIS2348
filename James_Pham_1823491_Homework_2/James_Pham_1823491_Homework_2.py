import datetime

# Create a dictionary to store month name as key and month number as value
month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
              'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
              'November': 11, 'December': 12}

today = datetime.datetime.now()
currentYear = today.strftime("%Y")

# Try to open file 
try:

    # Open parsedDates.txt file to write the parsed dates
    outFile = open('parsedDates.txt', 'w')

    # Open inputDates.txt file to read the dates
    with open('inputDates.txt', 'r') as file:

        # Loop for each date in file 
        for date in file:

            # Remove the trailing newline 
            date = date.strip()

            # If date is -1 
            if date == '-1':
                # Exit from loop
                break

                # Find the index of the space at the end of month name
            monthIndex = date.find(" ")

            # Find the index of the ', ' in the date string after month name 
            dayIndex = date[monthIndex + 1:].find(", ")

            # If the month index and day index is not -1 
            if monthIndex != -1 and dayIndex != -1:
                # Extract the month name from date string
                month = date[:monthIndex]

                # Extract the day from date string 
                day = date[monthIndex + 1:][:dayIndex]

                # Extract the year from date string 
                year = date[monthIndex + 1:][dayIndex + 2:]

                # Find the month number from month dictionary
                monthNum = month_dict[month]

                # remove date if year is > current year
                outFile.write(str(monthNum) + '/' + day + '/' + year + '\n')



# If file can't open 
except FileNotFoundError:

    # Print an error message 
    print('Error: Input file not found')
