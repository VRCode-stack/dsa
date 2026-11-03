a = [[1, 2], [3, 4], [5, 6]]
while True:
    print("\n1.Display 2.Insert 3.Delete 4.Search 5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        for row in a: print(row)
    elif ch == 2:
        r = int(input("Row index: "))
        c = int(input("Column index: "))
        x = int(input("Value: "))
        a[r].insert(c, x)
    elif ch == 3:
        r = int(input("Row index: "))
        c = int(input("Column index: "))
        if 0 <= r < len(a) and 0 <= c < len(a[r]): a[r].pop(c)
        else: print("Invalid position")
    elif ch == 4:
        x = int(input("Search value: "))
        print([(i, row.index(x)) for i, row in enumerate(a) if x in row] or "Not found")
    else:
        break

