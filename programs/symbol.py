rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of colums: "))
symbol = input("Enter symbol to be used: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()