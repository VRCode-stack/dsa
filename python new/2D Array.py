matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def display():
    print("Matrix:")
    for row in matrix:
        print(row)


while True:
    print("\n1. Insert Row")
    print("2. Delete Row")
    print("3. Search Element")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        pos = int(input("Enter row position (starting from 0): "))
        row = list(map(int, input("Enter 3 elements separated by space: ").split()))
        matrix.insert(pos, row)
        print("Row inserted")
    elif ch == 2:
        pos = int(input("Enter row position to delete: "))
        if 0 <= pos < len(matrix):
            matrix.pop(pos)
            print("Row deleted")
        else:
            print("Invalid position")
    elif ch == 3:
        key = int(input("Enter element to search: "))
        found = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == key:
                    print("Element", key, "found at row", i, "column", j)
                    found = True
        if not found:
            print("Element not found")
    elif ch == 4:
        display()
    elif ch == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
