# Define the menu of the restaurant
menu = {
    'Pizza': 40,
    'Burger': 30,
    'Sandwich': 25,
    'Salad': 20,
    'Fries': 15,
    'Coffee': 80,
    'Tea': 70,
    'Soda': 60,
    'Ice Cream': 50,
    'Cake': 45
}

# Greet
print("Welcome to the Python Restaurant!")
print('\n'.join(f"{item} : Rs{price}" for item, price in menu.items()))

order_total = 0

# Ask for first order
item_1 = input("Enter name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print("Sorry, we don't have that item in our menu")

# Ask for more items
another_order = input("Do you want to add another item? (Yes/No) ")
while another_order.lower() == "yes":
    input_2 = input("Enter the name of the item = ")
    if input_2 in menu:
        order_total += menu[input_2]
        print(f"Item {input_2} has been added to your order")
    else:
        print("Sorry, we don't have that item in our menu")
    another_order = input("Do you want to add another item? (Yes/No) ")

# Show total
print(f"The total amount of your order is Rs{order_total}")
