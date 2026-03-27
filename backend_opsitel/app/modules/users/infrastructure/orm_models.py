import uuid

from sqlalchemy import Column, String

from app.shared.infrastructure.database import Base


class Role:
    ADMIN = "admin"
    USER = "revisor"
    EDITOR = "editor"


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(String, default="true")
    role = Column(String, default=Role.USER)

