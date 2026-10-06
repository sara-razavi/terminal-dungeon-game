# Terminal Dungeon Game

player = {
    "name": "",
    "room": "start"
}

# every room has a description and what is on the left / right
rooms = {
    "start": {
        "desc": "You are in a dark room. Water drips from the ceiling.",
        "left": "armory",
        "right": "hall"
    },
    "armory": {
        "desc": "You are in an old armory. All the weapons are broken.",
        "left": "cellar",
        "right": "start"
    },
    "cellar": {
        "desc": "You are in a cold cellar. It smells terrible here.",
        "left": None,
        "right": "armory"
    },
    "hall": {
        "desc": "You are in a long hall with torches on the walls.",
        "left": "start",
        "right": "library"
    },
    "library": {
        "desc": "You are in a dusty library. Books are everywhere.",
        "left": "hall",
        "right": None
    }
}


def show_menu():
    print()
    print(rooms[player["room"]]["desc"])
    print()
    print("1. Go left")
    print("2. Go right")
    print("3. Check inventory")
    print("4. Leave")


def get_choice():
    choice = input("> ")
    return choice.strip()


def start_game():
    print("=== DUNGEON ===")
    name = input("What is your name? ")
    if name.strip() == "":
        name = "Stranger"
    player["name"] = name.strip()
    print("Welcome,", player["name"])


def move(direction):
    current = rooms[player["room"]]
    next_room = current[direction]

    if next_room == None:
        print("There is just a wall there.")
    else:
        player["room"] = next_room
        print("You go", direction + ".")


def main():
    start_game()

    running = True
    while running:
        show_menu()
        choice = get_choice()

        if choice == "1":
            move("left")
        elif choice == "2":
            move("right")
        elif choice == "3":
            # TODO real inventory
            print("Your inventory is empty.")
        elif choice == "4":
            print("You leave the dungeon. Bye", player["name"])
            running = False
        else:
            print("I don't understand that.")


main()
