from pydantic import BaseModel
from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from phoonbook_service.src.service import phonebook_service


phonebook_router_v1 = APIRouter(prefix="/phonebook")


class Person(BaseModel):
    phonebook_id: int
    last_name: str
    first_name: str
    phone_number: str
    info: str


class Phonebook(BaseModel):
    user_id: int
    phonebook_id: int
    contacts: list[Person]


@phonebook_router_v1.post("/{user_id}/upload-phonebook")
async def upload_phonebook(file: UploadFile, user_id: int):
    print(type(file.filename))
    return await phonebook_service.get_file(filename=file.filename, user_id=user_id)


@phonebook_router_v1.get("/{user_id}")
async def get_list_phonebooks(user_id: int):
    return await phonebook_service.get_list_phonebooks(user_id=user_id)


@phonebook_router_v1.get("/{user_id}/{phonebook_id}/contacts")
async def get_contact_phonebook(user_id: int, phonebook_id: int):
    return await phonebook_service.get_contact_phonebook(user_id=user_id, phonebook_id=phonebook_id)


@phonebook_router_v1.get("/{user_id}/{phonebook_id}/contacts/{person_id}")
async def get_contact_person_id(user_id: int, phonebook_id: int, person_id: int):
    return


@phonebook_router_v1.get("/{user_id}/{phonebook_id}/contacts/{last_name}")
async def get_contact_last_name(user_id: int, phonebook_id: int, last_name: str):
    return await phonebook_service.get_contact_last_name(user_id=user_id, phonebook_id=phonebook_id)


@phonebook_router_v1.get("/{user_id}/{phonebook_id}/contacts/{phone_number}")
async def get_contact_phone_number(user_id: int, phonebook_id: int, phone_number: str):
    return await phonebook_service.get_contact_phone_number(user_id=user_id, phonebook_id=phonebook_id,
                                                            phone_number=phone_number)


@phonebook_router_v1.post("/{user_id}/{phonebook_id}/{Person}")
async def insert_contact(user_id: int, phonebook_id: int, contact: Person):
    return await phonebook_service.insert_contact(user_id=user_id, phonebook_id=phonebook_id, contact=Person)


@phonebook_router_v1.get("/{user_id}/{phonebook_id}/downloads")
async def post_phone_book(user_id, phonebook_id):
    file = save_file("phonebook.csv", Phonebook.contacts)
    return FileResponse(path="phonebook.csv", filename="phonebook.csv")
