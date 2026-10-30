subject = int(input("Enter the number of row: "))

for x in range(0, subject):
    for y in range(0, subject - x - 1):
        print(" ", end="")
    for y in range(0, x + 1):
        print("* ", end="")
    print()

for x in range(0, subject - 1):
    for y in range(0, x + 1):
        print(" ", end="")
    for y in range(0, subject - x - 1):
        print("* ", end="")
    print()
