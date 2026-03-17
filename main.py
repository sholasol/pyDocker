from fastapi import FastAPI
from src.db.connection import init_db
from contextlib import asynccontextmanager  


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Initializing server...")
    try:
        await init_db()
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    yield
    print("🛑 Server shutting down...")

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Initializing server...")
#     await init_db()
#     yield
#     print("Server shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def main():
    return {"message": "Hello World"}





