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


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None
for key in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, key)
print("BST created with keys: [50, 30, 70, 20, 40, 60, 80]")
print("Inorder Traversal   :", end=" ")
inorder(root)
print()
print("Postorder Traversal :", end=" ")
postorder(root)
print()

