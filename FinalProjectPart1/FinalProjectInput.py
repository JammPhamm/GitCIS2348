# Pham, James 1823491 Final Project Part 1
import csv

with open('ManufacturerList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[1])
print()
with open('PriceList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[1])
print()
with open('ServiceDatesList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[1])