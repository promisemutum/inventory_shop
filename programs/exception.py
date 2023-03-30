numerator = int(input("Enter the numerator: "))
denomenator = int(input("Enter the denomenator: "))

try:
    result = numerator/denomenator
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("The result is "+ str(result))
finally:
    print("You have reached the end.")