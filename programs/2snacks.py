def snacks(people):
    chips_per_person = 0.5  
    soda_per_person = 0.25 
    bags_of_chips = round(people * chips_per_person)
    bottles_of_soda = round(people * soda_per_person)
    return bags_of_chips, bottles_of_soda

people = int(input("Number of people coming: "))
bags_of_chips, bottles_of_soda = snacks(people)
print(f"For {people} people, you should buy {bags_of_chips} bags of chips and {bottles_of_soda} bottles of soda.")