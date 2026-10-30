rows = int(input("Enter row number: "))

for x in range(0, rows):
    for y in range(0, rows - x - 1):
        print(" ", end="")
    for y in range(0, x + 1):
        print("* ", end="")
    print()

for x in range(0, rows - 1):
    for y in range(0, x + 1):
        print(" ", end="")
    for y in range(0, rows - x - 1):
        print("* ", end="")
    print()
