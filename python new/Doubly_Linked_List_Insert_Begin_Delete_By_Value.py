class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def _append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def create(self, values):
        for v in values:
            self._append(v)
        print("List created with values:", values)

    def display(self):
        if self.head is None:
            print("Doubly Linked List: Empty")
            return
        print("Doubly Linked List: NULL", end=" <-> ")
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        print("Inserted", data, "at beginning")

    def delete_value(self, value):
        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next
        if temp is None:
            print(value, "not found in list")
            return
        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev
        print("Deleted", value)


dl = DoublyLinkedList()
dl.create([10, 20, 30])
dl.display()
dl.insert_beginning(5)
dl.display()
dl.delete_value(20)
dl.display()
dl.delete_value(99)
dl.delete_value(5)
dl.display()
