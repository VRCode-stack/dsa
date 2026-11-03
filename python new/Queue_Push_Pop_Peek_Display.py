class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.front > self.rear

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, x):
        if self.is_full():
            print("Queue is Full! Cannot insert", x)
            return
        self.rear += 1
        self.queue[self.rear] = x
        print(x, "enqueued")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        print(self.queue[self.front], "dequeued")
        self.front += 1

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue (front to rear):", self.queue[self.front:self.rear + 1])


q = Queue(5)
print("Is queue empty?", q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print("Is queue full?", q.is_full())
q.display()
q.dequeue()
q.dequeue()
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print("Is queue empty?", q.is_empty())
