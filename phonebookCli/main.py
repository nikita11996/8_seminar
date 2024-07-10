import asyncio

from utils import print_person, save_file
from service import pars_data_file, find_by_person, add_person
from models import Person


async def show_menu():
    print("\nВыберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
          "2. Найти абонента по фамилии\n",
          "3. Найти абонента по номеру телефона\n",
          "4. Добавить абонента в справочник\n",
          "5. изменить данные\n",
          "6. Сохранить справочник в текстовом формате\n",
          "7. Закончить работу\n"
          )
    choice = int(input())
    return choice


async def work_with_phonebook():
    choice = await show_menu()
    phone_book = await pars_data_file('phon.txt')
    while (choice != 7):
        if choice == 1:
            await print_person(phone_book)
        elif choice == 2:
            last_name = input('lastname')
            search_person = await find_by_person(phonebook=phone_book, last_name=last_name)
            await print_person(search_person)
        elif choice == 3:
            phone_number = input('phone number')
            search_person = await find_by_person(phonebook=phone_book, phone_number=phone_number)
            await print_person(search_person)
        elif choice == 4:
            person = Person(
                last_name=input('last name'),
                first_name=input('first name'),
                phone_number=input('phone number'),
                info=input('info')
            )
            await add_person(phone_book, person)
        elif choice == 5:
            person = await find_by_person(phonebook=phone_book, last_name=input('last name'))
            phone_book[phone_book.index(person[0])] = Person(
                first_name=input('first name') if input('first name') != "" else person[0].first_name,
                last_name=input('last name') if input('last name') != "" else person[0].last_name,
                phone_number=input('phone number') if input('phone number') != "" else person[0].phone_number,
                info=input('info') if input('info') != "" else person[0].info
            )
        elif choice == 6:
            await save_file('phonebook.txt', phone_book)

        choice = await show_menu()


if __name__ == '__main__':
    asyncio.run(work_with_phonebook())
