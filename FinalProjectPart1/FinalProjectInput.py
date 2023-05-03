# Pham, James 1823491 Final Project Part 1
import csv
from datetime import date

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


# Sort merged data by item_id
def get_itemID(item):
    return item[0]


sorted_data = sorted(merged_data.items(), key=get_itemID)

# Create separate CSV files based on item_type
for item_type in set([x[1]['item_type'] for x in sorted_data]):
    filename = f"{item_type.capitalize()}Inventory.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in sorted_data:
            if item[1]['item_type'] == item_type:
                row = [item[0], item[1]['manufacturer'], item[1]['price'], item[1]['service_date'], item[1]['damaged']]
                writer.writerow(row)

# Get the current date
today = date.today()

# Extract items with service date in the past
past_service_date_items = []
for item_id, item_data in merged_data.items():
    if 'service_date' in item_data:
        service_date_str = item_data['service_date']
        service_date_parts = service_date_str.split('/')
        service_date = date(int(service_date_parts[2]), int(service_date_parts[0]), int(service_date_parts[1]))
        if service_date < today:
            item_data['service_date'] = service_date.strftime('%m/%d/%Y')
            past_service_date_items.append((item_id, item_data))


# Sort items by service date
def get_service_date(item):
    return item[1]['service_date']

sorted_data = sorted(past_service_date_items, key=get_service_date)

# Write data to CSV file
with open('PastServiceDateInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i, item_data in enumerate(sorted_data):
        item_id = sorted_data[i][0]
        writer.writerow([item_id, item_data[1]['manufacturer'], item_data[1]['item_type'], item_data[1]['price'],
                         item_data[1]['service_date'], item_data[1]['damaged']])

# Define a function to get the price
def get_price(item):
    return float(item[1]['price'])

# Sort merged data by price
sorted_data = sorted(merged_data.items(), key=get_price, reverse=True)

# Write sorted data to a new CSV file
with open('DamagedInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for item in sorted_data:
        if item[1]['damaged'] == 'damaged':
            writer.writerow(
                [item[0], item[1]['manufacturer'], item[1]['item_type'], item[1]['price'], item[1]['service_date'], item[1]['damaged']])
