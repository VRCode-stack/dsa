class Node:
    def __init__(self, x): self.key, self.left, self.right = x, None, None
def insert(r, x):
    if not r: return Node(x)
    if x < r.key: r.left = insert(r.left, x)
    else: r.right = insert(r.right, x)
    return r
def inorder(r):
    if r: inorder(r.left); print(r.key, end=" "); inorder(r.right)

root = None
for x in [40, 20, 60, 10, 30]: root = insert(root, x)
inorder(root)

