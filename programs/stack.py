from collections import deque
from queue import LifoQueue

#using list
def list_stack():
    stack = []
    i = ''
    con = "y"
    while con == "y":
        i = input("Enter-\nPress 1 to Push element.\nPress 2 to Pop element.\nPress 3 to View size.\nPress 4 to View top.\nPress 5 to check if stack is empty.\n-")
        if i == '1':
            temp = input("Enter element to push: ")
            stack.append(temp)
            print(stack)
        elif i == '2':
            if stack != []:
                stack.pop()
            print(stack)
        elif i == '3':
            temp = len(stack)
            print(temp)
        elif i == '4':
            print(stack[-1])
        elif i == '5':
            if stack == []:
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        con = input("Do you want to continue operations?y: ")

#using deque
def deque_stack():
    stack = deque()
    con = "y"
    while con == "y":
        i = input("Enter-\nPress 1 to Push element.\nPress 2 to Pop element.\nPress 3 to View size.\nPress 4 to View top.\nPress 5 to check if stack is empty.\n-")
        if i == '1':
            temp = input("Enter element to push: ")
            stack.append(temp)
            print(stack)
        elif i == '2':
            if len(stack) != 0:
                stack.pop()
            print(stack)
        elif i == '3':
            temp = len(stack)
            print(temp)
        elif i == '4':
            print(stack[-1])
        elif i == '5':
            if len(stack) == 0:
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        else:
            print("Error")
        con = input("Do you want to continue operations?y: ")

#using queue
def queue_stack():
    stack = LifoQueue()
    con = "y"
    while con == "y":
        i = input("Enter-\nPress 1 to Push element.\nPress 2 to Pop element.\nPress 3 to View size.\nPress 4 to View top.\nPress 5 to check if stack is empty.\n-")
        if i == '1':
            temp = input("Enter element to push: ")
            stack.put(temp)
            print(stack.queue)
        elif i == '2':
            if stack.qsize() != 0:
                stack.get()
            print(stack.queue)
        elif i == '3':
            print(stack.qsize())
        elif i == '4':
            print(stack.queue[-1])
        elif i == '5':
            if stack.qsize() == 0:
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        else:
            print("Error")
        con = input("Do you want to continue operations?y: ")

#main
print("Start stack program")
i = input("Press 1 to use list\nPress 2 to use deque\nPress 3 to use queue\n-")
if i == '1':
    list_stack()
elif i == '2':
    deque_stack()
elif i == '3':
    queue_stack()

    

