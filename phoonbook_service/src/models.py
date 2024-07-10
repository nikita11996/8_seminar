import asyncio
from phoonbook_service.src.storage.storage import PhonebookStorage

asyncio.run(PhonebookStorage.create_table())