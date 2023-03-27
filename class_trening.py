contacts = []

class Menuitem:
    def __init__(self, title, handler):
        self.title = title
        self.handler = handler


def add_contact_mode():
    name = input("Name >>> ")
    num = input("Number >>> ")
    contact = {name: num}
    return contacts.append(contact)

def show_book():
    return contacts

def del_contact():
    name = input("Name >>> ")
    del contacts[name]

def print_menu(name_menu, menu):
    num_item = 0
    print(name_menu)
    for i in menu:
        num_item += 1
        print(f"{num_item} - {i.title}")


main_menu = [Menuitem("Adding a new contact...", add_contact_mode),
             Menuitem("Display list of contacts...", show_book),
             Menuitem("Delete selected contact...", del_contact)]           

print_menu("_____MENU_____", main_menu)