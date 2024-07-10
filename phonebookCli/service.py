from models import Person
from tabulate import tabulate

from utils import read_file, save_file


async def pars_data_file(filename):
    contact = []
    content = await read_file(filename)
    for line in content.splitlines():
        if len(line) > 1:
            list_person = line.split(", ")
            for i in range(len(list_person)):
                list_person[i] = list_person[i].replace("\t", "")
            contact.append(Person(
                list_person[1],
                list_person[0],
                list_person[2],
                list_person[3])
            )
    return contact


async def find_by_person(phonebook: list, last_name: str = None, phone_number: str = None) -> list[Person]:
    result_person = []
    if last_name is None:
        for person in phonebook:
            if phone_number in person.phone_number:
                result_person.append(person)
    else:
        for person in phonebook:
            if last_name in person.last_name:
                result_person.append(person)
    return result_person


async def add_person(phonebook: list, person: Person):
    phonebook.append(person)
    print("Добавлен абонент в справочник")
    return phonebook
