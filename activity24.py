from activity23 import your_screen_time
from activity23 import ask_my_name
from activity23 import box


while True:
    print("SELECT AN OPINION")
    print("1 - your_screen_time")
    print("2 - ask_my_name")
    print("3 - box")
    print("4 - Exit")

    choose = int(input("Please type your choice --> "))

    if choose == 1:
        print("Screen Time")
        num = int(input("Enter your screen time"))
        print(your_screen_time(num))
        continue
    elif choose == 2:
        print("Your Name")
        name = input("Enter your name --> ")
        ask_my_name(name)
        continue
    elif choose == 3:
        print("Box")
        num = int(input("Enter the size of the box"))
        box(num)
        continue
    elif choose == 4:
        print("System Exit")
        break
    else:
        print("Invalid choice")
        continue