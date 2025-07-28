# Define the menu of restaurant
menu = {
    'Pizza':120,
    'Coffee':80,
    'Salad':55,
    'Burger':60,
    'Tea':15,
}
# Greet
print("Welcome to FIZZA Restaurant")

# Display menu 
print("Pizza  : Rs120\nCoffee : Rs80\nSalad  : Rs55\nBurger : Rs60\nTea    : Rs15")

order_total = 0


# take order
item_1  = input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you Want to add another item? (Yes/No) : ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is ₹{order_total}")
