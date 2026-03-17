from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(pg.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    first_name: Mapped[str] = mapped_column(String, index=True)
    last_name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String, default="user")
    is_verified: Mapped[bool] = mapped_column(pg.BOOLEAN, default=False)
    created_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    
    

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

