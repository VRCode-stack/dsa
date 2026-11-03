class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

def insert(r, x):
    if not r: return Node(x)
    if x < r.key: r.left = insert(r.left, x)
    elif x > r.key: r.right = insert(r.right, x)
    return r

def search(r, x):
    if not r or r.key == x: return r
    return search(r.left, x) if x < r.key else search(r.right, x)

def delete(r, x):
    if not r: return r
    if x < r.key: r.left = delete(r.left, x)
    elif x > r.key: r.right = delete(r.right, x)
    else:
        if not r.left: return r.right
        if not r.right: return r.left
        p = r.right
        while p.left: p = p.left
        r.key = p.key; r.right = delete(r.right, p.key)
    return r

def inorder(r):
    if r: inorder(r.left); print(r.key, end=" "); inorder(r.right)

root = None
for x in [50, 30, 70, 20, 40, 60, 80]: root = insert(root, x)
inorder(root); print()
print("Found" if search(root, 40) else "Not found")
root = delete(root, 30); inorder(root); print()

