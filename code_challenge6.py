#size = eval(input("Input of x ----> "))

for x in range(5): #size
    for y in range(5): #size
    #line 2 and line 1
        if x + y == 4 or x == y:
            print("*", end = " ")
        else:
            print(" ", end = " ")      
    print()
