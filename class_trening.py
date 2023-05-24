class ContactRecord:
    def __init__(self, id: int,surname: str, name: str, father_name: str, email: str):
        self.id = id
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.email = email

contacts = []

for i in range(10):
    contacts.append(ContactRecord(1, "Lisimenko", "Alexandr", "Igorevich", "lis@mail.ru"))

def filter_func(list):
    index = 0
    first_cont = list[index]
    for contact in list[1:]:
        if first_cont.surname == contact.surname and first_cont.name == contact.name and first_cont.father_name == contact.father_name and first_cont.email == contact.email:
            list.remove(contact)
        else:
            index += 1
    return list

print(filter_func(contacts))