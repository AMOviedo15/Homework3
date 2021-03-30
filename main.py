# Aaron Oviedo 1990958

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" +
              str(self.item_price * self.item_quantity))


if __name__ == '__main__':
    print("Item 1")
    useritem1 = ItemToPurchase()
    print('Enter the item name:')
    useritem1.item_name = input()
    print('Enter the item price:')
    useritem1.item_price = int(input())
    print('Enter the item quantity:')
    useritem1.item_quantity = int(input())

    print("\nItem 2")
    useritem2 = ItemToPurchase()
    print('Enter the item name:')
    useritem2.item_name = input()
    print('Enter the item price:')
    useritem2.item_price = int(input())
    print('Enter the item quantity:')
    useritem2.item_quantity = int(input())

    print("\nTOTAL COST")
    useritem1.print_item_cost()
    useritem2.print_item_cost()

    total = (useritem1.item_price * useritem1.item_quantity) + (useritem2.item_price * useritem2.item_quantity)

    print("\nTotal: $" + str(total))