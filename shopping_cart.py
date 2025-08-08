# Step 1: ItemToPurchase Class

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
    
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}")

# Step 2: Main Program with User Input

def main():
    # Create two shopping items
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    
    # Get item 1 details from user
    print("Item 1")
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    
    # Get item 2 details from user
    print("\nItem 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    
    # Calculate and print total cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total}")

if __name__ == "__main__":
    main()
