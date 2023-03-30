number = input("Enter the number: ")

def reverse1(num):
    newNum = 0
    while num > 0:
        remainder = num % 10 
        newNum = newNum * 10 + remainder
        num //= 10
    return newNum

#better
def reverse2(num):
    newNum = (str(num)[::-1])
    return newNum

print(reverse2(num = number))
