class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(n):
    return n.height if n else 0


def balance(n):
    return height(n.left) - height(n.right) if n else 0


def update(n):
    n.height = 1 + max(height(n.left), height(n.right))


def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update(y)
    update(x)
    return x


def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    update(x)
    update(y)
    return y


def rebalance(n):
    update(n)
    b = balance(n)
    if b > 1:
        if balance(n.left) < 0:
            print("   Left-Right (LR) rotation at node", n.key)
            n.left = rotate_left(n.left)
        else:
            print("   Left-Left (LL) rotation at node", n.key)
        return rotate_right(n)
    if b < -1:
        if balance(n.right) > 0:
            print("   Right-Left (RL) rotation at node", n.key)
            n.right = rotate_right(n.right)
        else:
            print("   Right-Right (RR) rotation at node", n.key)
        return rotate_left(n)
    return n


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return rebalance(root)


def inorder(n):
    return inorder(n.left) + [n.key] + inorder(n.right) if n else []


def preorder(n):
    return [n.key] + preorder(n.left) + preorder(n.right) if n else []


print("Case 1: LL rotation - inserting 30, 20, 10")
root = None
for key in [30, 20, 10]:
    root = insert(root, key)
print("Preorder:", preorder(root), " Inorder:", inorder(root))

print()
print("Case 2: RR rotation - inserting 10, 20, 30")
root = None
for key in [10, 20, 30]:
    root = insert(root, key)
print("Preorder:", preorder(root), " Inorder:", inorder(root))

print()
print("Case 3: LL rotation in a bigger tree - inserting 40, 20, 60, 10, 5")
root = None
for key in [40, 20, 60, 10, 5]:
    root = insert(root, key)
print("Preorder:", preorder(root), " Inorder:", inorder(root))

print()
print("Case 4: RR rotations - inserting 10, 20, 30, 40, 50")
root = None
for key in [10, 20, 30, 40, 50]:
    root = insert(root, key)
print("Preorder:", preorder(root), " Inorder:", inorder(root))
