class Child:
    def __init__(self, name, age, gender, height, weight):
        self.name= name
        self.age = age
        self.gender= gender
        self.height= height
        self.weight= weight
        
    def calculate_bmi(self):
            bmi= self.weight/ (self.height**2)
            return bmi
        
    def  min_daily_calories(self):
        if self.age <= 2:
            return 800
        elif self.age <=4:
            return 1400
        elif self.age<= 8:
            return 1800
        else:
            return "Invalid age range"
        
    def daily_calorie_consumption(self, food_list):
        total_calories = 0
        food_calories = {"Milk" : 100, "egg" : 155, "rice" : 130, "lentils" : 113, "vegetable" : 85, "meat": 143} 
        for food, quantity in food_list.items():
            total_calories += food_calories [food] * (quantity /100)
            return total_calories
        
        
    def check_nourishment(self, food_list):
        min_calories = self.min_daily_calories()
        consumed_calories = self.daily_calorie_consumption(food_list)
        if consumed_calories < min_calories:
            return "Undernourished"
        else:
            return  "well-nourished"
        
print("Child Nutrition Calculator")
name = input("Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
height = float(input("Height: "))
weight = float(input("Weight: "))
Child1 = Child(name , age, gender, height, weight)
print(Child1.calculate_bmi())
print(Child1.min_daily_calories())
milk = int(input("Milk: "))
egg = int(input("Egg: "))
rice = int(input("Rice: "))
lentils = int(input("Lentils: "))
vegetable = int(input("Vegetable: "))
meat = int(input("Meat: "))
food_list = {"Milk": milk, "egg" : egg, "rice" :rice, "lentils": lentils, "vegetable" :vegetable, "meat" :meat}
print (Child1.daily_calorie_consumption(food_list))
print(Child1.check_nourishment(food_list))