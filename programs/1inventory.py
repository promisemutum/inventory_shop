#You are running a small convenience store and want to keep track of your inventory. 
#Can you write a program that allows you to add and remove items from your inventory, and displays the current stock?
inventory = {}
#inventory={'Soap': 7, 'Rice': 6, 'Jeera': 9}

def add():
    temp1 = str(input("Enter the product name:"))
    if temp1 in inventory.keys():
        temp2 = int(input("Enter the quantity to be added:"))
        inventory[temp1]=inventory[temp1]+temp2
    else:
        temp2 = int(input("Enter the quantity:"))
        inventory[temp1]=temp2

def remove():
    temp1 = str(input("Enter the product name:"))
    if temp1 in inventory.keys():
        temp2 = int(input("Enter the quantity to be removed:"))
        if inventory[temp1]>temp2:
            inventory[temp1]=inventory[temp1]-temp2
        elif inventory[temp1]==temp2:
            del inventory[temp1]
        else:
            print("Amount to be removed is more.")
    else:
        print("Item not found.")

print("Welcome to the inventory")
temp3 = "n"
while temp3!="y":
    i = int(input("Press 1 for adding items\nPress 2 for removing items"))
    if i==1:
        add()
        print(inventory)
    elif i==2:
        remove()
        print(inventory)
    else:
        print("Invalid option")
        print(inventory)
    temp3 = str(input("Do you wanna quit?y/n: "))