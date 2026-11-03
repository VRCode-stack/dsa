class Node:
    def __init__(self, x): self.data, self.left, self.right = x, None, None
def info(n):
    if not n: return 0
    lh, rh = info(n.left), info(n.right)
    h = 1 + max(lh, rh)
    print(n.data, "Height:", h, "Balance Factor:", lh-rh)
    return h
root = Node(1)
root.left = Node(2); root.right = Node(3)
root.left.left = Node(4); root.left.right = Node(5)
info(root)