class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head
        print("Inserted", data, "at end")

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
        print("Inserted", data, "at beginning")

    def display(self):
        if self.head is None:
            print("Circular List: Empty")
            return
        print("Circular List:", end=" ")
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head " + str(self.head.data) + ")")


cl = CircularLinkedList()
cl.insert_end(10)
cl.insert_end(20)
cl.insert_end(30)
cl.display()
cl.insert_beginning(5)
cl.display()
