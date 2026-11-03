class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def analyse(root, info):
    if root is None:
        return 0
    lh = analyse(root.left, info)
    rh = analyse(root.right, info)
    h = 1 + max(lh, rh)
    info.append((root.data, h, lh - rh))
    return h


def is_bst(root, low, high):
    if root is None:
        return True
    if root.data <= low or root.data >= high:
        return False
    return is_bst(root.left, low, root.data) and is_bst(root.right, root.data, high)


def check(root, name):
    print(name)
    info = []
    analyse(root, info)
    print("Node   Height   Balance Factor")
    for data, h, bf in info:
        print(str(data).ljust(7) + str(h).ljust(9) + str(bf))
    balanced = all(-1 <= bf <= 1 for _, _, bf in info)
    if balanced and is_bst(root, float("-inf"), float("inf")):
        print("Result: The tree is an AVL tree")
    else:
        print("Result: The tree is NOT an AVL tree")
    print()


tree1 = Node(40, Node(20, Node(10), Node(30)), Node(60, Node(50), Node(70)))
tree2 = Node(40, Node(20, Node(10, Node(5)), Node(30)), Node(60))

check(tree1, "Tree 1 (nodes listed bottom-up):")
check(tree2, "Tree 2 (nodes listed bottom-up):")
