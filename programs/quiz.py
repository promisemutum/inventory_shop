import sys
def new():
    guesses = []
    correctguess = 0
    qnum = 1
    for key in questions:
        print(" ")
        print(key)
        for i in options[qnum-1]:
            print(i)
        guess = input("A or B: ")
        guess = guess.upper()
        guesses.append(guess)
        correctguess += check(questions.get(key), guess)
        qnum += 1
    view(correctguess)
def check(answer, guess):
    if answer == guess:
        print("Correct answer")
        return 1
    else:
        print("Wrong answer")
        return 0
def view(answer):
    print("Number of correct answers: "+str(answer))
def retry():
    again = input("Do you want to try again?y/n: ")
    if again == "y":
        new()
    elif again == "n":
        sys.exit("Thank you for taking the quiz!")
    else:
        print("Invalid input")
questions = {
    "What is your name":"B",
    "What is your age":"A"
}
options = [["A. Jack","B. Pro"],
            ["A. 18","B. 16"]]
start = input("Start the quiz???y/n: ")
if start == "y":
    new()
    while 1:
        retry()
elif start == "n":
    exit
else:
    print("Invalid input")