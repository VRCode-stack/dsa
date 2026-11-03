class Node:
    def __init__(self, k):
        self.k, self.l, self.r, self.h = k, None, None, 1
def height(n): return n.h if n else 0
def right_rotate(y):
    x, t = y.l, y.l.r
    x.r = y; y.l = t
    y.h = 1 + max(height(y.l), height(y.r))
    x.h = 1 + max(height(x.l), height(x.r))
    return x
def left_rotate(x):
    y, t = x.r, x.r.l
    y.l = x; x.r = t
    x.h = 1 + max(height(x.l), height(x.r))
    y.h = 1 + max(height(y.l), height(y.r))
    return y
def insert(n, k):
    if not n: return Node(k)
    if k < n.k: n.l = insert(n.l, k)
    elif k > n.k: n.r = insert(n.r, k)
    else: return n
    n.h = 1 + max(height(n.l), height(n.r))
    b = height(n.l) - height(n.r)
    if b > 1 and k < n.l.k: return right_rotate(n)       # LL
    if b < -1 and k > n.r.k: return left_rotate(n)       # RR
    if b > 1 and k > n.l.k:                              # LR
        n.l = left_rotate(n.l); return right_rotate(n)
    if b < -1 and k < n.r.k:                             # RL
        n.r = right_rotate(n.r); return left_rotate(n)
    return n
def inorder(n):
    if n: inorder(n.l); print(n.k, end=" "); inorder(n.r)

root = None
for x in [30, 20, 10, 25, 28, 27]: root = insert(root, x)
inorder(root)


