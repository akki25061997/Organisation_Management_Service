from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

orgs_col = db["organizations"]
admins_col = db["admins"]

async def init_indexes():
    await orgs_col.create_index("organization_name", unique=True)
    await admins_col.create_index("email", unique=True)
