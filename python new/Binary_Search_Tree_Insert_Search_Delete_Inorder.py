class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)


def min_node(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = min_node(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root


def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


root = None
while True:
    print("\n--- BST MENU ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display (Inorder)")
    print("5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        key = int(input("Enter value to insert: "))
        if search(root, key) is not None:
            print(key, "already exists")
        else:
            root = insert(root, key)
            print(key, "inserted")
    elif ch == 2:
        key = int(input("Enter value to search: "))
        if search(root, key) is not None:
            print(key, "found in the tree")
        else:
            print(key, "not found in the tree")
    elif ch == 3:
        key = int(input("Enter value to delete: "))
        if search(root, key) is None:
            print(key, "not found, cannot delete")
        else:
            root = delete(root, key)
            print(key, "deleted")
    elif ch == 4:
        result = []
        inorder(root, result)
        print("Inorder:", result)
    elif ch == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")


