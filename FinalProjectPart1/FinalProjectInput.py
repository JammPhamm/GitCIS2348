# Pham, James 1823491 Final Project Part 1
import csv

with open('ManufacturerList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_ManufacturerList.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)
