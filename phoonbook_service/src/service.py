# from routers import Phonebook, Person
from dataclasses import dataclass

from phoonbook_service.src.storage.storage import PhonebookStorage
from phoonbook_service.src.storage.database import async_session_factory
from aiofiles import open


# async def read_file(filename):
#     async with open(file=filename, mode="r") as f:
#         return await f.read()
#
# async def main():
#     content = await read_file("phon.txt")
#     for line in content.splitlines():
#         if len(line) > 1:
#             list_person = line.split(", ")
#             for i in range(len(list_person)):
#                 list_person[i] = list_person[i].replace("\t", "")
#             person = Person(list_person[0], list_person[1], list_person[2], list_person[3])
#             print(person.__str__())
#             await save_file("text.txt", person.__repr__())

@dataclass
class Person:
    phonebook_id: int
    last_name: str
    first_name: str
    phone_number: str
    info: str

@dataclass
class Phonebook:
    user_id: int
    phonebook_id: int
    contacts: list[Person]



class Service:
    @staticmethod
    async def get_file(filename: str, user_id: int):
        await PhonebookStorage.add_users_phonebook(async_session=async_session_factory, user_id=user_id)
        phonebook_id = await PhonebookStorage.get_number_last_phonebook(async_session=async_session_factory, user_id=user_id)
        contacts = []
        async with open(file=filename, mode="r") as f:
            file_content = await f.read()
            for line in file_content.splitlines():
                if len(line) > 1:
                    person_data = [i.replace("\t", "") for i in line.split(", ")]
                    contacts.append(Person(
                        phonebook_id=phonebook_id,
                        last_name=person_data[0],
                        first_name=person_data[1],
                        phone_number=person_data[2],
                        info=person_data[3],
                    ))
            await PhonebookStorage.insert_contact(async_session=async_session_factory, contact=contacts)
        return contacts

    async def get_contact_phonebook(self, user_id: int, phonebook_id: int) -> list[Person] | str:
        if phonebook_id in await PhonebookStorage.get_phonebooks(async_session=async_session_factory, user_id=user_id):
            contact = await PhonebookStorage.get_contacts(
                async_session=async_session_factory,
                phonebook_id=phonebook_id
            )
            contact_list = []
            for i in contact:
                contact_list.append(Person(
                    phonebook_id=i.phonebook_id,
                    last_name=i.last_name,
                    first_name=i.first_name,
                    phone_number=i.number_telephone,
                    info=i.info
                ))
            return contact_list
        else:
            return "Phonebook not found"

    async def get_list_phonebooks(self, user_id: int) -> list[Phonebook] | str:
        return await PhonebookStorage.get_phonebooks(async_session=async_session_factory, user_id=user_id)

    async def get_contact_last_name(self, user_id: int, phonebook_id: int, last_name: str) -> Person | str:
        if phonebook_id in PhonebookStorage.get_phonebooks(async_session=async_session_factory, user_id=user_id):
            return await PhonebookStorage.get_contacts_by_last_name(
                last_name=last_name,
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"

    async def get_contact_phone_number(self, user_id: int, phonebook_id: int, phone_number: str) -> str:
        if phonebook_id in PhonebookStorage.get_phonebooks(async_session=async_session_factory, user_id=user_id):
            return await PhonebookStorage.get_contacts_by_phome_number(
                async_session=async_session_factory,
                phone_number=phone_number,
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"

    async def get_contact_person_id(self, user_id: int, phonebook_id: int, person_id: int) -> Person | str:
        if phonebook_id in PhonebookStorage.get_phonebooks(async_session=async_session_factory, user_id=user_id):
            return await PhonebookStorage.get_contacts_by_person_id(async_session=async_session_factory, person_id=person_id)
        else:
            return "Phonebook not found"


phonebook_service = Service()
