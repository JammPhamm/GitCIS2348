import csv
from datetime import date

# Read and merge data from CSV files
merged_data = {}
for filename in ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            item_id = line[0]
            item_data = merged_data.setdefault(item_id, {})
            if filename == 'ManufacturerList.csv':
                item_data['manufacturer'] = line[1]
                item_data['item_type'] = line[2]
                item_data['damaged'] = line[3]
            elif filename == 'PriceList.csv':
                item_data['price'] = float(line[1])
            elif filename == 'ServiceDatesList.csv':
                item_data['service_date'] = date.fromisoformat(line[1])


# Define a function to get the most expensive item by item type and manufacturer
def get_most_expensive_item(item_type, manufacturer):
    items = [(item_id, item_data) for item_id, item_data in merged_data.items()
             if item_data['item_type'] == item_type and item_data['manufacturer'] == manufacturer
             and 'damaged' not in item_data and 'service_date' not in item_data]
    if not items:
        return None
    most_expensive_item = max(items, key=lambda x: x[1]['price'])
    return most_expensive_item


# Loop to query user input
while True:
    # Get manufacturer and item type from user
    input_str = input("Enter manufacturer and item type separated by a space (or 'q' to quit): ")
    if input_str.lower() == 'q':
        break
    input_parts = input_str.strip().split()
    if len(input_parts) != 2:
        print("Invalid input. Please enter manufacturer and item type separated by a space.")
        continue
    manufacturer, item_type = input_parts

    # Get most expensive item and similar item from another manufacturer
    most_expensive_item = get_most_expensive_item(item_type, manufacturer)
    if most_expensive_item is None:
        print("No such item in inventory.")
        continue
    similar_item = None
    for item_id, item_data in merged_data.items():
        if item_data['item_type'] == item_type and item_data['manufacturer'] != manufacturer \
                and 'damaged' not in item_data and 'service_date' not in item_data:
            if similar_item is None or abs(item_data['price'] - most_expensive_item[1]['price']) < \
                    abs(similar_item[1]['price'] - most_expensive_item[1]['price']):
                similar_item = (item_id, item_data)

    # Print output
    print("Your item is:", most_expensive_item[0], manufacturer, item_type, most_expensive_item[1]['price'])
    if similar_item is not None:
        print("You may also consider:", similar_item[0], similar_item[1]['manufacturer'], item_type,
              similar_item[1]['price'])
