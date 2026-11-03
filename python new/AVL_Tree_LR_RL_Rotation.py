class Node:
    def __init__(self, k):
        self.k = k
        self.left = self.right = None
        self.h = 1

def height(n):
    return n.h if n else 0

def insert(root, k):
    if not root:
        return Node(k)

    if k < root.k:
        root.left = insert(root.left, k)
    elif k > root.k:
        root.right = insert(root.right, k)

    root.h = 1 + max(height(root.left), height(root.right))
    b = height(root.left) - height(root.right)

    if b > 1:
        if k > root.left.k:
            x = root.left
            root.left = x.right
            x.right = root
            root.h = 1 + max(height(root.left), height(root.right))
            x.h = 1 + max(height(x.left), height(x.right))
            return x

    if b < -1:
        if k < root.right.k:
            y = root.right
            root.right = y.left
            y.left = root
            root.h = 1 + max(height(root.left), height(root.right))
            y.h = 1 + max(height(y.left), height(y.right))
            return y

    return root

# LR example
root = None
for x in [30, 10, 20]:
    root = insert(root, x)
print("LR result:", root.k)

# RL example
root = None
for x in [10, 30, 20]:
    root = insert(root, x)
print("RL result:", root.k)
