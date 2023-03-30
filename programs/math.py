import math

print("First Investment")
principle1 = float(input("Enter the Principle Amount "))
interest1 = float(input("Enter the Interest Amount "))
duration1 = float(input("Enter the time "))

amt1 = int(math.ceil(principle1+((principle1*interest1*duration1)/100)))
print("First Amount: " + str(amt1))

print("Second Investment")
principle2 = float(input("Enter the Principle Amount "))
interest2 = float(input("Enter the Interest Amount "))
duration2 = float(input("Enter the time "))

amt2 = math.ceil(principle2+((principle2*interest2*duration2)/100))
print("Second Amount: " + str(amt2))

if amt1 > amt2 :
    print("First Investment has more profit")
    print("Amount of profit is " + str(amt1 - principle1))
elif amt1 == amt2 :
    print("Both amounts are same")
else:
    print("Second Investment has more profit")
    print("Amount of profit is " + str(amt2 - principle2))


