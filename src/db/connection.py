from sqlalchemy.ext.asyncio import create_async_engine
from src.config import CONFIG
from sqlalchemy import text
from .models import Base, User

# Ensure the protocol is correct for asyncpg
DB_URL = f"postgresql+asyncpg://{CONFIG.postgres_user}:{CONFIG.postgres_password}@db:5432/{CONFIG.postgres_db}"

engine = create_async_engine(
    url=DB_URL, 
    echo=True,
    pool_pre_ping=True # Checks if connection is alive before using it
)

async def init_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            print("Database initialized and tables created")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise e