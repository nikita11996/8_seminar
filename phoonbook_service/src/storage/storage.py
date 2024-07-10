from phoonbook_service.src.storage.database import async_session_factory, Base, async_engine
# from database import async_session_factory
from sqlalchemy.ext.asyncio import async_session, AsyncSession, async_sessionmaker
from sqlalchemy import select
from phoonbook_service.src.storage.models import Phonebook, Contact
# from routers import Person


class PhonebookStorage:

    @staticmethod
    async def create_table():
        async with async_engine.begin() as session:
            await session.run_sync(Base.metadata.drop_all)
            await session.run_sync(Base.metadata.create_all)

    @staticmethod
    async def add_users_phonebook(async_session: async_sessionmaker[AsyncSession], user_id: int):
        async with async_session() as session:
            data = Phonebook(user_id=user_id)
            session.add(data)
            await session.commit()

    @staticmethod
    async def get_number_last_phonebook(async_session: async_sessionmaker[AsyncSession], user_id: int) -> object:
        async with async_session() as session:
            quere = select(Phonebook).where(Phonebook.user_id == user_id)
            res = await session.execute(quere)
            result = res.scalars().all()[-1]
        return result.phonebook_id
    @staticmethod
    async def get_contacts(async_session: async_sessionmaker[AsyncSession], phonebook_id: int):
        async with async_session() as session:
            quere = select(Contact).where(Contact.phonebook_id == phonebook_id)
            res = await session.execute(quere)
            result = res.scalars().all()
        return result
    @staticmethod
    async def get_phonebooks(async_session: async_sessionmaker[AsyncSession], user_id: int):
        async with (async_session() as session):
            quere = select(Phonebook.phonebook_id).where(Phonebook.user_id == user_id)
            res =await session.execute(quere)
            result = res.scalars().all()
        return result

    @staticmethod
    async def insert_contact(async_session: async_sessionmaker[AsyncSession], contact: [Contact] or Contact):
        print(type(contact))
        if type(contact) != type([]):
            data = Contact(
                phonebook_id=contact.phonebook_id,
                first_name=contact.first_name,
                last_name=contact.last_name,
                number_telephone=contact.phone_number,
                info=contact.info)
            async with async_session() as session:
                session.add(data)
            await session.commit()
        else:
            async with async_session() as session:
                for i in contact:
                    print(i)
                    data = Contact(
                        phonebook_id=i.phonebook_id,
                        first_name=i.first_name,
                        last_name=i.last_name,
                        number_telephone=i.phone_number,
                        info=i.info)
                    session.add(data)
                await session.commit()

    @staticmethod
    async def get_contacts_by_last_name(async_session: async_session_factory, last_name: str, phonebook_id: int):
        async with async_session() as session:
            quere = select(Contact).where(Contact.last_name == last_name and Contact.phonebook_id == phonebook_id)
            return await session.execute(quere).scalars().all()

    @staticmethod
    async def get_contacts_by_phome_number(async_session: async_session_factory, phone_number: str, phonebook_id: int):
        async with async_session() as session:
            quere = select(Contact).where(Contact.last_name == phone_number and Contact.phonebook_id == phonebook_id)
            return await session.execute(quere).scalars().all()

    @staticmethod
    async def get_contacts_by_person_id(async_session: async_session_factory, person_id: str):
        async with async_session() as session:
            quere = select(Contact).where(Contact.id == person_id)
            return await session.execute(quere).scalars().all()
