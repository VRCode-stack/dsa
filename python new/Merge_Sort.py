def merge_sort(a):
    if len(a) <= 1: return a
    m = len(a)//2
    l, r = merge_sort(a[:m]), merge_sort(a[m:])
    out = []
    while l and r: out.append(l.pop(0) if l[0] < r[0] else r.pop(0))
    return out + l + r

a = list(map(int, input("Enter numbers: ").split()))
print("Before:", a)
print("After: ", merge_sort(a))


