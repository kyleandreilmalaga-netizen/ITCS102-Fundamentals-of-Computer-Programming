screen_time = int(input("Enter how manny hours you spending in your mobile phone? --> "))

def your_screen_time(answer):
    screen = 1 
    for x in range(answer, 0, -1):
        screen *= x 
    return screen

def ask_my_name (yourname):
    name = "my name is " + yourname
    print(name)

def box(num):
    for x in range (num+1):
        for y in range(num+1):
            if x == 0 or y == 0 or x == num or y == num:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()


print("output", your_screen_time(14))
print("output", your_screen_time(13))
print("output", your_screen_time(12))
print("output", your_screen_time(11))
print("output", your_screen_time(10))
print("output", your_screen_time(9))
print("output", your_screen_time(8))
print("output", your_screen_time(7))
print("output", your_screen_time(6))
print("output", your_screen_time(5))
print("output", your_screen_time(4))
print("output", your_screen_time(3))
print("output", your_screen_time(2))
print("output", your_screen_time(1))


ask_my_name("Kyle")
ask_my_name("Andrei")
ask_my_name("Laroyaa")
ask_my_name("Malaga")

