import datetime
# Shopping Cart Project

foods=[]
prices=[]
total=0
clientName=""
storeName="EMT Groceries"
date=datetime.datetime.now()

clientName=input("Enter Your First Name: ")

while True:
    food=input("Enter a food that you want to buy or q to quit: ")
    if food.lower()=="q":
     break
    else:
     price=float(input(f"Enter the price of your {food}: R"))
     foods.append(food)
     prices.append(price)

print("\n")
print("-------Your Cart-------")

for food in foods:
    print(food)

for price in prices:
    total += price
    
print("\n")
print(f"Your Total is: R{total}")
print("\n")
print(f"Thank You {clientName} For Shopping At {storeName}.😊❤️")
print(date)
print("\n")

