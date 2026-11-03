class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, x):
        if len(self.stack) == self.size:
            print("Stack Overflow! Cannot push", x)
            return
        self.stack.append(x)
        print(x, "pushed")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow! Stack is empty")
            return
        print(self.stack.pop(), "popped")

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return
        print("Top element is", self.stack[-1])

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return
        print("Stack (top to bottom):", self.stack[::-1])


s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.display()

