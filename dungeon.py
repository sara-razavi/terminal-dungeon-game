# Terminal Dungeon Game

player = {
    "name": "",
    "room": "start"
}


def show_menu():
    print()
    print("You are in a dark room.")
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


def main():
    start_game()

    running = True
    while running:
        show_menu()
        choice = get_choice()

        if choice == "1":
            print("You go left, but it is just a wall.")
        elif choice == "2":
            print("You go right, nothing here too.")
        elif choice == "3":
            # TODO real inventory
            print("Your inventory is empty.")
        elif choice == "4":
            print("You leave the dungeon. Bye", player["name"])
            running = False
        else:
            print("I don't understand that.")


main()
