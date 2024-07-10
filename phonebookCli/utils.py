from aiofiles import open
from tabulate import tabulate

from models import Person


async def read_file(filename) -> str:
    async with open(file=filename, mode="r") as f:
        return await f.read()


async def save_file(filename: str, phonebook: list) -> None:
    async with open(file=filename, mode="w") as f:
        await f.write("")
    async with open(file=filename, mode="a") as f:
        for person in phonebook:
            await f.write(person.__repr__() + "\n")


async def print_person(phonebook: list):
    print(tabulate(phonebook, headers='keys', tablefmt='psql'))
    # for i in phonebook:
    #     print(i.__str__())
