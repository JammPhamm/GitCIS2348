# Pham, James 1823491 Final Project Part 2

import csv
from datetime import datetime

# Read data from CSV files
merged_data = {}
with open('FullInventory.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header
    for item_id, manufacturer, item_type, price, service_date, damaged in reader:
        merged_data[item_id] = {
            'item_id': item_id,
            'manufacturer': manufacturer,
            'item_type': item_type,
            'price': float(price),
            'service_date': datetime.strptime(service_date, '%m/%d/%Y').date(),
            'damaged': damaged == 'damaged',
        }

# Group items by item type
items_by_type = {}
for item in merged_data.values():
    if not item['damaged'] and item['service_date'] >= datetime.today().date():
        item_type = item['item_type']
        if item_type not in items_by_type:
            items_by_type[item_type] = []
        items_by_type[item_type].append(item)

# Print items in inventory
print(merged_data)

# Interactive inventory query capability
while True:
    query = input("Enter manufacturer and item type (e.g. Apple computer): ")
    if query == 'q':
        break

    manufacturer, item_type = query.strip().split(' ', 1)
    candidate_items = [item for item in items_by_type.get(item_type, [])
                       if item['manufacturer'].lower() == manufacturer.lower()]

    if not candidate_items:
        print("No such item in inventory")
    elif len(candidate_items) > 1:
        print("More than one item matches the query")
    else:
        item = candidate_items[0]
        print(f"Your item is: {item['item_id']}, {item['manufacturer']}, {item['item_type']}, {item['price']}")
        closest_item = None
        closest_price_diff = float('inf')
        for other_item in items_by_type.get(item_type, []):
            if other_item is not item and not other_item['damaged'] and other_item['service_date'] >= datetime.today().date():
                price_diff = abs(item['price'] - other_item['price'])
                if price_diff < closest_price_diff:
                    closest_item = other_item
                    closest_price_diff = price_diff
        if closest_item is not None:
            print(f"You may also consider: {closest_item['manufacturer']}, {closest_item['item_type']}, {closest_item['price']}")
