# Reuse the AVL code from Program 19.
# LR example:
root = None
for x in [30, 10, 20]: root = insert(root, x)
print("LR result:", root.k)   # 20
# RL example:
root = None
for x in [10, 30, 20]: root = insert(root, x)
print("RL result:", root.k)   # 20


