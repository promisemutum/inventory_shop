# You are a teacher and want to grade your students' exams. Can you write a program that takes in
#a list of scores and calculates the average, minimum, and maximum grades?
def grade(scores):
    average=int(sum(scores)/len(scores))
    minimum=min(scores)
    maximum=max(scores)
    return average, minimum, maximum

students=int(input("Number of students:"))
scores=[]
for i in range(0,students):
    temp = int(input("enter mark:"))
    scores.append(temp)
average,minimum,maximum=grade(scores)
print(f"Average grade is: {average}")
print(f"Minimum grade is: {minimum}")
print(f"Maximum grade is: {maximum}")