import os

location = "C:\\Users\\Blaze Pro\\Documents\\notes\\pythontest.txt"

if os.path.exists(location):
    print("The path exists!")
    if os.path.isfile(location):
        print("It is a file!")
        with open(location) as file:
            print("Contents:"+file.read())
            switch = int(input("1. Enter 1 to overwrite data.\n2. Enter 2 to add data\n3. Enter 3 to exit.\n-"))
            if switch == 1:
                with open(location,'w') as file:
                    file.write(input("Enter the text: ")) 
            elif switch == 2:
                with open(location,'a') as file:
                    file.write(input("Enter the text: "))
            else: pass
            print("...End...")
    elif os.path.isdir(location):
        print("It is a folder!")
else:
    print("The path doesn't exist!")