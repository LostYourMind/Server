# DBControl.py

from databases import Database
from .DataBaseDef import DATABASE_URL

database = Database(DATABASE_URL)

async def connect_db():
    await database.connect()

async def disconnect_db():
    await database.disconnect()

async def fetch_one(query: str, values: dict = {}):
    result = await database.fetch_one(query=query, values=values)
    return result

async def execute(query: str, values: dict):
    result = await database.execute(query=query, values=values)
    return result
