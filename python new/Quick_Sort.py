def quick_sort(a):
    if len(a) <= 1: return a
    p = a[len(a)//2]
    left = [x for x in a if x < p]
    mid = [x for x in a if x == p]
    right = [x for x in a if x > p]
    return quick_sort(left) + mid + quick_sort(right)

a = list(map(int, input("Enter numbers: ").split()))
print("Before:", a)
print("After: ", quick_sort(a))


