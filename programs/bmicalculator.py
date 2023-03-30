x = int(input("Enter weight of the child:"))
y = int(input("Enter height of the child:"))
bmi = x/(y**2)
if (bmi<16):
    print("Severly Underweight")
elif ((bmi>=16)and(bmi<18.5)):
    print("Underweight")
elif ((bmi>=18.5)and(bmi<25)):
    print("Underweight")

