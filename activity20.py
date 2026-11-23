anime = []
answer = input("Do you watch anime? (yes/no) --> ").lower()

while True:
    if answer == "yes":
        title = input("What is the title of the anime? --> ")
        anime.append(title)
        ans = input("Is there anything else? (yes/no) --> ").lower()
    else:
        print(anime)
        break
