a = list(map(int, input("Enter numbers: ").split()))
x = int(input("Search: "))
for i in range(len(a)):
    if a[i] == x:
        print("Found at index", i); break
else:
    print("Not found")


