class CircularQueue():
    def __init__(self,k):
        self.k = k
        self.len = 0
        self.queue = [None]*k
        self.front = self.rear = -1

    def EnQueue(self,data):
        if(self.rear+1)%self.k == self.front:
            print("The queue is full")
            return False
        else:
            rear = (self.rear+1)%self.k
            self.queue[rear] = data
            self.rear = rear
            self.len += 1
            if self.len == 1:
                self.head = 0
            return True

    def DeQueue(self):
        if(self.head == -1):
            print("The circular queue is empty")
        elif(self.head == self.rear):
            temp = self.queue[self.head]
            self.head = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1)%self.k
            return temp
    
    def PrintQueue(self):
        if(self.head == -1):
            print("The circular queue is empty.")
        elif(self.rear >= self.head):
            for i in range(self.head, self.rear+1):
                print(self.queue[i], end=", ")
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=", ")
            for i in range(0, self.rear+1):
                print(self.queue[i],end=", ")

i = input("Enter size of the circular queue:")
q = CircularQueue(int(i))
for _ in range(int(i)):
    q.EnQueue(input("-"))
q.PrintQueue()
q.DeQueue()
q.PrintQueue()