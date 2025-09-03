def welcome_customer():
    """Gets the customer's name and welcomes customer"""
    print("---------- WELCOME TO MY GROCERY STORE ----------")
    name = input("Please enter your name to proceed: ")
    print("Hello", name, ", Let's begin shopping!")
    return name

# Inventory setup using concept of nested dictionary

inventory = {
    "Fruits": {
        "Apples": {"price": 1.25, "stock": 45},
        "Mangoes": {"price": 2.50, "stock": 34},
        "Bananas": {"price": 0.50, "stock": 40},
        "Guavas": {"price": 1.25, "stock": 60},
        "Strawberry Box": {"price": 3.00, "stock": 32},
    },
    "Vegetables": {
        "Potatoes": {"price": 1.00, "stock": 76},
        "Tomatoes": {"price": 1.25, "stock": 49},
        "Carrots": {"price": 0.55, "stock": 25},
        "Green Chillies": {"price": 0.25, "stock": 65},
    },
    "Frozen": {
        "Ice Cream": {"price": 3.0, "stock": 10},
        "Frozen Pizza": {"price": 5.5, "stock": 8},
    },
    "Other Eatables": {
        "Bread": {"price": 2.25, "stock": 10},
        "Milk": {"price": 3.5, "stock": 15},
        "Eggs": {"price": 4.0, "stock": 25},
    }
}

# Display inventory
def display_inventory(inventory):
    print("\n----------- THE ITEMS AVAILABLE WITH THE STORE ARE ----------")
    if not inventory:
        print("THE STORE IS CURRENTLY EMPTY :(")
    for category in inventory:
        print("\n-----", category, "------")
        for item in inventory[category]:
            price = inventory[category][item]["price"]
            stock = inventory[category][item]["stock"]
            print(item, "- Price: $", price, "| Stock:", stock)
    print("-" * 60)

# Add to cart
def add_to_cart_item(inventory, cart):
    while True:
        item_name = input("Enter the item name you want to add to your cart: ").strip().title()
        found = False
        for category in inventory:
            for item in inventory[category]:
                if item_name == item:
                    found = True
                    quantity = int(input("Enter quantity of " + item_name + ": "))
                    if quantity <= inventory[category][item]["stock"]:
                        if item in cart:
                            cart[item] += quantity
                        else:
                            cart[item] = quantity
                        inventory[category][item]["stock"] -= quantity
                        print(str(quantity) + " " + item + "(s) added to your cart :)")
                    else:
                        print("SORRY, WE ARE OUT OF STOCK :(")
                    break
            if found:
                break
        if not found:
            print("ITEM NOT FOUND. Please refer back to the inventory.")

        add_more = input("Do you want to add more items? Press y for YES and n for NO: ").lower()
        if add_more != "y":
            break

# View cart
def view_cart(cart):
    if not cart:
        print("YOUR CART IS EMPTY.")
        return
    print("\n---------- YOUR SHOPPING CART ----------")
    for item in cart:
        print(item + " : " + str(cart[item]))
    print("-" * 50)

# Checkout
def checkout(cart, inventory):
    if not cart:
        print("CART EMPTY. NOTHING TO CHECK OUT!")
        return
    total = 0
    print("\n---------- FINAL BILL ----------")
    for item in cart:
        for category in inventory:
            if item in inventory[category]:
                price = inventory[category][item]["price"]
                break
        quantity = cart[item]
        item_total = price * quantity
        print(item, "-", quantity, "x $", price, "=", "$", round(item_total, 2))
        total += item_total
    print("TOTAL BILL: $", round(total, 2))
    print("---------- THANK YOU FOR SHOPPING WITH US! -----------\n")

# Main
def main():
    name = welcome_customer()
    cart = {}
    while True:
        print("\nWhat would you like to do?")
        print("1. View Inventory")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            add_to_cart_item(inventory, cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart, inventory)
            break
        elif choice == "5":
            print("Goodbye,", name + "! Come back soon :)")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 5.")

main()
