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

contacts.append(ContactRecord(2, "Ivanov", "Aleksey", "Fedorovich", "alexey@mail.ru"))

def filter_func(list):
    index = 0
    first_cont = list[index]
    for contact in list[1:]:
        if first_cont.id == contact.id:
            list.remove(contact)
        else:
            index += 1
    return list

for i in filter_func(contacts):
    print(i.name)
