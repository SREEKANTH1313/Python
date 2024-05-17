import time
print("Welcome to Amigos Fruit_Juice Shop")
print("Please choose the menu and order your favourite items")
time.sleep(1)
fruits_menu = {"Apple": 50, "Banana": 35, "Badam": 45, "Pineapple": 35, "Mango": 40, "Orange": 30, "Grapes": 30, "Sapota": 40}
print("Munu      Price")
print("**---------------------**")
for menu, price in fruits_menu.items():
    print(f"{menu}   :  {price}")
    print("-------------------------")
time.sleep(1)
Total_Bill = 0
orders_list = []
while True:
    user = input("Enter Your Fav Juice Here: ").capitalize()
    if user in fruits_menu:
        quantity = int(input("Enter how many glasses you want: "))
        price = fruits_menu[user] *  quantity
        Total_Bill += price
        orders_list.append((user, quantity, price))
        chances = input("If you want another drink please enter 'yes' otherwise 'no': ").lower()
        if chances == "no":
            break
    else:
        print(f"your fav {user} juice is not available, please choose another one")
time.sleep(1)
print("\n Your Bill: ")
print(f"{'Drink':<10} {'Qty':<5} {'price':<5} {'Total':<10}")
for orders in orders_list:
    drink, qty, price = orders
    print(f"{drink:<10}  {qty:<5}  {fruits_menu[drink]:<5} {price:<5}")
print(f" Your Total Bill is:    {Total_Bill}")

