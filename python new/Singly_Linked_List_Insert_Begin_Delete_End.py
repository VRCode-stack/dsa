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

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Inserted", data, "at beginning")

    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        if self.head.next is None:
            print("Deleted", self.head.data, "from end")
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        print("Deleted", temp.next.data, "from end")
        temp.next = None


ll = SinglyLinkedList()
ll.insert_beginning(30)
ll.insert_beginning(20)
ll.insert_beginning(10)
ll.display()
ll.delete_end()
ll.display()
ll.delete_end()
ll.delete_end()
ll.display()
ll.delete_end()


