from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass


class Birthday(Field):
    pass


class Record(UserDict):

    def __init__(self, name, phone,  **kwargs) -> None:
        self.name = name
        self.phones = [phone]
        self.emails = []
        self.birthday = None
        for key, value in kwargs.items():
            if key == "email": self.emails.append(value)
            elif key == "birthday": self.birthday = value
        self.data = {
            "Name": self.name,
            "Phones": self.phones,
            "Emails": self.emails,
            "Birthday":self.birthday
        }

    
class AddrBook(UserDict):
    
    def add_contact(self, record):
        key = record.name.value
        value = record
        self[key] = value
