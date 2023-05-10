# Pham, James 1823491 Final Project Part 2
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
    item_manufacturer = item[1].lower()
    item_item_type = item[2].lower()
    if manufacturer in item_manufacturer and item_type in item_item_type:
        found_items.append(item)

# Print search results
if len(found_items) == 0:
    print("No such item in inventory")
elif len(found_items) == 1:
    print("Your item is: ")
    print(found_items[0])
else:
    print("Multiple items found. Please enter a more specific query.")
