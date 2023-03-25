contacts = []

class Menuitem:
    def __init__(self, title, handler):
        self.title = title
        self.handler = handler
        print(self.title)

def add_contact_mode():
    name = input("Name >>> ")
    num = input("Number >>>")
    contact = {name: num}
    return contacts.append(contact)

def show_book():
    return contacts

def del_contact():
    name = input("Name >>> ")
    del contacts[name]

main_menu = ["_____MENU_____",
             Menuitem("Adding a new contact...", add_contact_mode),
             Menuitem("Display list of contacts...", show_book),
             Menuitem("Delete selected contact...", del_contact)]           

