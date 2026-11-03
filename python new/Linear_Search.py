n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter " + str(n) + " elements: ").split()))
key = int(input("Enter element to search: "))

print("Array:", arr)
found = False
for i in range(n):
    if arr[i] == key:
        print("Element", key, "found at index", i, "(position", i + 1, ")")
        found = True
        break
if not found:
    print("Element", key, "not found in the array")


