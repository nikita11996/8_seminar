import os
from dotenv import load_dotenv

load_dotenv()

dsn = (f"postgresql+asyncpg://"
       f"{os.getenv('DB_LOGIN')}:"
       f"{os.getenv('DB_PSW')}@"
       f"{os.getenv('DB_HOST')}:"
       f"{os.getenv('DB_PORT')}/"
       f"{os.getenv('DB_NAME')}")
