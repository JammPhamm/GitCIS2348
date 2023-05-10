import csv

# Read FullInventory.csv
inventory = []
with open('FullInventory.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        inventory.append(row)

# Get user input
manufacturer = input("Enter the manufacturer: ").strip().lower()
item_type = input("Enter the item type: ").strip().lower()

# Search for item in inventory
found_items = []
for item in inventory:
    item_id = item[0]
    item_manufacturer = item[1].lower()
    item_item_type = item[2].lower()
    item_price = float(item[3])
    item_service_date = item[4]
    item_damaged = item[5].lower()
    if manufacturer in item_manufacturer and item_type in item_item_type and item_service_date == "" and item_damaged == "no":
        found_items.append([item_id, item_manufacturer, item_item_type, item_price])

# Print search results
if len(found_items) == 0:
    print("No such item in inventory")
else:
    most_expensive_item = found_items[0]
    for item in found_items:
        if item[3] > most_expensive_item[3]:
            most_expensive_item = item
    print("Your item is: ", most_expensive_item[0], most_expensive_item[1], most_expensive_item[2], most_expensive_item[3])

