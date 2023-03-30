import datetime
animals = {}

def add():
    temp1 = str(input("Enter the animal:"))
    temp2 = input("Enter the feeding time (in HH:MM format): ")
    temp3 = datetime.datetime.strptime(temp2, "%H:%M")
    nextfeeding = temp3 + datetime.timedelta(hours=6)
    temp4=nextfeeding.strftime("%H:%M")
    animals[temp1]=temp4

def remove():
    temp1 = str(input("Enter the animal:"))
    if temp1 in animals.keys():
        del animals[temp1]
    else:
        print("Item not found.")

print("Welcome to the zoo")
temp3 = "n"
while temp3!="y":
    i = int(input("Press 1 for adding animals\nPress 2 for removing animals"))
    if i==1:
        add()
        print(animals)
    elif i==2:
        remove()
        print(animals)
    else:
        print("Invalid option")
        print(animals)
    temp3 = str(input("Do you wanna quit?y/n: "))