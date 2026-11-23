# AKAME GA KILL
akame = ["Assassin of Night Raid", "Murasame (One-Cut Killer)"]
tatsumi = ["Member of Night Raid", "Incursio"]
esdeath = ["General of the Empire", "Demon's Extract"]
leone = ["Member of Night Raid", "Lionelle (Beast Transformation)"]


# INUYASHA
inuyasha = ["Half-demon", "Tessaiga"]
kagome = ["Priestess", "Sacred Arrows"]
sesshomaru = ["Full-blooded demon", "Bakusaiga"]
miroku = ["Buddhist monk", "Wind Tunnel"]


# KONOSUBA
kazuma = ["Adventurer", "Steal"]
megumin = ["Arch Wizard", "Explosion Magic"]
aqua = ["Goddess of Water", "Healing Magic"]
darkness = ["Crusader", "Exceptional Defense"]


# TENSURA
rimuru = ["Reincarnated as a slime", "Predator and Great Sage"]
benimaru = ["Leader of the ogres", "Black Flames"]
diablo = ["Primordial Black Demon", "Temptation World"]
shion = ["Ogre warrior", "Ogre Strength"]
akame_ga_kill = {"Akame": akame,"Tatsumi": tatsumi,"Esdeath": esdeath,"Leone": leone}
inuyasha_series = {"Inuyasha": inuyasha,"Kagome": kagome,"Sesshomaru": sesshomaru,"Miroku": miroku}
konosuba = {"Kazuma": kazuma,"Megumin": megumin,"Aqua": aqua,"Darkness": darkness}
tensura = {"Rimuru": rimuru,"Benimaru": benimaru,"Diablo": diablo,"Shion": shion}


old_anime = {"Akame ga Kill": akame_ga_kill,"Inuyasha": inuyasha_series}
new_anime = {"Konosuba": konosuba,"Tensura": tensura}

anime = {"Old Anime": old_anime,"New Anime": new_anime}

print("=== 1. Going down one level at a time ===")
print(anime["Old Anime"]["Akame ga Kill"]["Akame"][1])

print()

print("=== 2. Loop level 1: categories ===")
for category in anime:
    print(category)

print()

print("=== 3. Loop levels 1-2: categories and titles ===")
for category, titles in anime.items():
    print(category)
    for title in titles:
        print(" -", title)

print()

print("=== 4. Loop ALL levels ===")
for category, titles in anime.items():
    print(category)
    for title, characters in titles.items():
        print("  " + title)
        for name, info in characters.items():
            print("    " + name)
            print("      Description:", info[0])
            print("      Power:", info[1])

print()

print("=== 5. Count every character ===")
count = 0
for titles in anime.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1

print("Total characters:", count)

print()

print("=== 6. Search for a character ===")
search = "Rimuru"
found = False

for category, titles in anime.items():
    for title, characters in titles.items():
        if search in characters:
            print(search, "is from", title, "(" + category + ")")
            print("Power:", characters[search][1])
            found = True

if found == False:
    print(search, "not found.")
