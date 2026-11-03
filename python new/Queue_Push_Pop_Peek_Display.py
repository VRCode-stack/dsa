q, SIZE = [], 5
def enqueue(x):
    if len(q) == SIZE: print("Full")
    else: q.append(x)
def dequeue():
    print(q.pop(0) if q else "Empty")
def isEmpty(): print(len(q) == 0)
def isFull(): print(len(q) == SIZE)
def display(): print(q)

enqueue(10); enqueue(20); display(); dequeue(); display()
isEmpty(); isFull()

