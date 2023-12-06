"""
Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.
"""

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(self.name, self.email, self.phone, self.favorite)
        
        return copy_obj


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(self.filename, self.contacts)
        
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts)
        copy_obj.contacts = copy.deepcopy(self.contacts, memo)
        copy_obj.is_unpacking = copy.deepcopy(self.is_unpacking, memo)
        copy_obj.count_save = copy.deepcopy(self.count_save, memo)
        
        return copy_obj


if __name__ == '__main__':

    person = Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    )

    e_person = copy.copy(person)
    print(person.name)
    print(e_person.name)

    # e = Expenses()
    # e.spent('hotel', 100)
    # e.spent('taxi', 10)
    # print(e.places)  # ['hotel', 'taxi']

    # e_copy = copy(e)
    # print(e_copy is e)  # False
    # e_copy.spent('bar', 30)
    # print(e.places)  # ['hotel', 'taxi', 'bar']

    print('Done...')
