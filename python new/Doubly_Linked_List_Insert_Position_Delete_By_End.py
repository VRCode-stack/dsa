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

    def insert_end(self, data):
        self._append(data)
        print("Inserted", data, "at end")

    def insert_position(self, pos, data):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            print("Inserted", data, "at position", pos)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                break
            temp = temp.next
        if temp is None or pos < 1:
            print("Invalid position", pos)
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        print("Inserted", data, "at position", pos)

    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        print("Deleted", temp.data, "from end")
        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None


dl = DoublyLinkedList()
dl.insert_position(1, 10)
dl.insert_position(2, 30)
dl.insert_position(2, 20)
dl.insert_position(4, 40)
dl.display()
dl.insert_position(9, 99)
dl.delete_end()
dl.display()
dl.delete_end()
dl.delete_end()
dl.delete_end()
dl.display()
dl.delete_end()
