#bool variable

sub = True

while sub == True:
    ask = input("Do you want to continue --> ")

    if ask.lower() == "Yes":
        print("You chose to continue...")
        continue
    else:
        print("You chose to STOP")
        break