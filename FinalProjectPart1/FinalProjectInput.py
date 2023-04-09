# Pham, James 1823491 Final Project Part 1
import csv

merged_data = {}

# Read ManufacturerList.csv
with open('ManufacturerList.csv', 'r') as file:
    for line in file:
        item_id, manufacturer, item_type, damaged = line.strip().split(',')
        merged_data.setdefault(item_id, {}).update({
            'manufacturer': manufacturer,
            'item_type': item_type,
            'damaged': damaged,
        })

# Read PriceList.csv
with open('PriceList.csv', 'r') as file:
    for line in file:
        item_id, price = line.strip().split(',')
        merged_data.setdefault(item_id, {}).update({
            'price': price,
        })

# Read ServiceDatesList.csv
with open('ServiceDatesList.csv', 'r') as file:
    for line in file:
        item_id, service_date = line.strip().split(',')
        merged_data.setdefault(item_id, {}).update({
            'service_date': service_date,
        })


# Define a function to get the manufacturer name
def get_manufacturer(item):
    return item[1]['manufacturer']


# Sort merged data by manufacturer name
sorted_data = sorted(merged_data.items(), key=get_manufacturer)

# Write sorted data to a new CSV file
with open('FullInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for item in sorted_data:
        writer.writerow(
            [item[0], item[1]['manufacturer'], item[1]['item_type'], item[1]['price'], item[1]['service_date'],
             item[1]['damaged']])
