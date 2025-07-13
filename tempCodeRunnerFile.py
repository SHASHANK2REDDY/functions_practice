from datetime import datetime
print(datetime.now())
Customer_name=input("enter the your name:")
items='''
    mango: 50/kg,
    apple: 30/kg,
    banana: 20/kg,
    orange: 40/kg,
    grapes: 60/kg,
    watermelon: 70/kg,
    pineapple: 80/kg,
    strawberry: 90/kg,
    kiwi: 100/kg
'''
print(items)
price=0
items_buy=[]
total_price=0
final_price=0
qlist=[]
plist=[]
#item_list=['mango','apple','banana','orange','grapes','watermelon','pineapple','strawberry','kiwi']
market_items = {
    'mango': 50,'apple': 30,'banana': 20,'orange': 40,
    'grapes': 60,'watermelon': 70,'pineapple': 80,'bag':28,'strawberry': 90,'kiwi': 100}
enter=int(input("enter the number of items you want to buy:"))
while enter!=0:
    print("enter 1 to buy items:")
    print("enter 2 to exit the market")
    print("enter 3 for bill generation")
    choice = int(input("enter your choice:"))
    if choice==2:
        print("Thanks for Visiting: ")
        break
    elif choice == 1:
        print(market_items)
        while choice!=3:
           item = input("enter the item you want to buy:")
           if item in market_items:
               qty=float(input("enter the quantity of the item:"))
               price=qty * market_items.get(item)
               plist.append(price)
               qlist.append(qty)
               total_price=total_price+market_items.get(item)
               print(item,":",market_items.get(item))
               print(f"Price for {qty} kg of {item} is: {price}")
               choice=input("enter the choice:")
           else:
               print("the item is not found in the market")
               continue
        while choice==3:
            print("Total price of the items you bought is:", total_price)
            final_price = total_price - ((total_price * 18) / 100)
            print("Final price after discount is:", final_price)