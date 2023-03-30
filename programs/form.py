#form
name = ""
id = ""
address = ""

while len(name) == 0:
    name = str(input("Enter your name: "))
    id = str(input("Enter your id: "))
    address = str(input("Enter your address: "))

print("Name: " + name + " ,ID: " + id + " ,Address: " + address)