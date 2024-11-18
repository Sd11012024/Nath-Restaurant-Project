# Define the menu of the restaurant
menu = {
    'Chicken Biriyani': 100,
    'Mutton Biriyani': 150,
    'Aloo Biriyani': 70,
    'Egg Biriyani': 80,
    'Egg Roll': 30,
    'Chicken Roll': 50,
    'Double Egg Roll': 70,
    'Chowmin': 40,
    'Muglai': 45,
    'Fried Rice': 100,
    'Chilly Chicken': 80,
    'Salad': 20,
}

# Greet
print("Welcome to Nath Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: {price}")

order_total = 0

# Take the first order
item_1 = input(
    "\nEnter the name of the item you want to order: ").strip().title()
if item_1 in menu:
    order_total += menu[item_1]  # Add price to the total
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, the item '{item_1}' is not available.")

# Ask if the customer wants another order
another_order = input(
    "\nDo you want to add another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]  # Add price to the total
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available.")

# Display the total amount
print(f"\nThe total amount to pay is: {order_total}")
