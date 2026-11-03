class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        print(x, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow! Stack is empty")
            return
        print(self.top.data, "popped")
        self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        print("Top element is", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        print("Stack (top to bottom):", end=" ")
        temp = self.top
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()
s.pop()
s.pop()
s.pop()
s.display()

