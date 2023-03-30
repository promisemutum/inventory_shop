#queue

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) != 0:
            self.queue.pop()
    
    def display(self):
        print(self.queue)

q = Queue()
y = 'y'
while y == 'y':
    i = input("1. Enqueue\n2. Dequeue\n3. Print\n-")
    if i == '1':
        q.enqueue(input("Enter element:"))
    elif i == '2':
        q.dequeue()
    elif i == '3':
        q.display()
    y = input("Press y to continue:")
else: 
    print("Bye")
    exit()

