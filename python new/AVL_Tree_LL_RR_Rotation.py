# Reuse the AVL code from Program 19.
# LL example:
root = None
for x in [30, 20, 10]: root = insert(root, x)
print("LL result:", root.k)   # 20
# RR example:
root = None
for x in [10, 20, 30]: root = insert(root, x)
print("RR result:", root.k)   # 20

