# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run 
from datetime import datetime

print(datetime.now())
Customer_name = input("Enter your name: ")

items = '''
    mango: ₹50/kg,
    apple: ₹30/kg,
    banana: ₹20/kg,
    orange: ₹40/kg,
    grapes: ₹60/kg,
    watermelon: ₹70/kg,
    pineapple: ₹80/kg,
    strawberry: ₹90/kg,
    kiwi: ₹100/kg
'''
print("Available items:")
print(items)

# Global variables
price = 0
items_buy = []
total_price = 0
final_price = 0
qlist = []
plist = []

market_items = {
    'mango': 50, 'apple': 30, 'banana': 20, 'orange': 40,
    'grapes': 60, 'watermelon': 70, 'pineapple': 80,
    'strawberry': 90, 'kiwi': 100
}

# Function to exit
def exit_market():
    print("Thanks for visiting, {}".format(Customer_name))

# Function to buy items
def buy_item():
    global total_price
    item = input("Enter the item: ").strip().lower()
    if item in market_items:
        qty = float(input("Enter the quantity in kg: "))
        price = market_items[item] * qty
        total_price += price
        qlist.append(qty)
        plist.append(price)
        items_buy.append(item)
        print(f"Item: {item}, Quantity: {qty}kg, Price: ₹{price}")
    else:
        print("The item is not found in the market.")

# Function to generate bill
def generate_bill():
    global total_price, final_price
    tax = total_price * 0.18
    discount = total_price * 0.10
    final_price = total_price + tax - discount
    print("\n------ BILL ------")
    print(f"Customer Name: {Customer_name}")
    for i in range(len(items_buy)):
        print(f"{items_buy[i]} - {qlist[i]}kg : ₹{plist[i]}")
    print(f"Subtotal  -  -  : ₹{total_price}")
    print(f"Tax (18%):  -  ₹{tax}")
    print(f"Discount (10%): ₹{discount}")
    print(f"Final Price to Pay: ₹{final_price}")

# Main loop
while True:
    print("\nEnter 1 to buy items")
    print("Enter 2 to generate bill")
    print("Enter 3 to exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        buy_item()
    elif choice == 2:
        generate_bill()
        break
    elif choice == 3:
        exit_market()
        break
    else:
        print("Invalid choice. Please try again.")
"""thanks for visiting, {Customer_name}"""