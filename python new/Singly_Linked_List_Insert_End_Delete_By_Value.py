class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List: Empty")
            return
        print("Linked List:", end=" ")
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print("Inserted", data, "at end")

    def delete_value(self, value):
        temp = self.head
        if temp is None:
            print("List is empty, nothing to delete")
            return
        if temp.data == value:
            self.head = temp.next
            print("Deleted", value)
            return
        while temp.next is not None and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print(value, "not found in list")
        else:
            temp.next = temp.next.next
            print("Deleted", value)


ll = SinglyLinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.display()
ll.delete_value(30)
ll.display()
ll.delete_value(99)
ll.delete_value(10)
ll.display()
