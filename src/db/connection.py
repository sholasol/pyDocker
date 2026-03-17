from sqlalchemy.ext.asyncio import create_async_engine
from src.config import CONFIG
from sqlalchemy import text


DB_URL = f"postgresql+asyncpg://{CONFIG.postgres_user}:{CONFIG.postgres_password}@db/{CONFIG.postgres_db}"
#replace localhost with db for docker
engine = create_async_engine(url=DB_URL, echo=True)

async def init_db():
    async with engine.begin() as conn:
        statement = text("""SELECT 'Connection successful' AS result""")
        result = await conn.execute(statement)
        print(result.all())
 