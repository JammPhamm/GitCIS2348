# Pham, James 10.19 zyLab
# ItemToPurchase class
class ItemToPurchase:
    # constructor + 3 attributes
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ $', end='')
        print(self.item_price, '= $', end='')

        cost = self.item_price * self.item_quantity
        print(cost)

    def print_item_description(self):
        print('{}:  {}'.format(self.item_name, self.print_item_description))


# main()
# driver code
class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2016"
        self.cart_items = list()

    def add_item(self):
        