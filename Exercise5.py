menu = {}


def add_item_to_menu():
    x = 0
    while x < 5:
        item_input = input("Add an Item to Menu: ")
        price_input = float(input("Set an Item Price: "))
        menu[item_input] = price_input
        x = x + 1
        add_item_choice = input("Want to add more? y/n \n")
        if add_item_choice == "n":
            break


def show_menu():
    print(menu)


if __name__ == "__main__":
    choice = ""
    while choice != "x":
        choice = input("Options\n"
                       "Choose a to Add Item:\n"
                       "Choose b to show Menu:\n"
                       "Choose x to Exit:\n")
        if choice == "a":
            add_item_to_menu()
        elif choice == "b":
            show_menu()
        elif choice == "x":
            exit()
