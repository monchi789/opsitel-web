import enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class Role(str, enum.Enum):
    ADMIN = "admin"
    USER = "revisor"
    EDITOR = "editor"


class UserBase(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    role: Role = Role.USER
    is_active: bool = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[Role] = None
    is_active: Optional[bool] = None
    password: Optional[str] = None


class User(UserBase):
    id: str

    model_config = ConfigDict(from_attributes=True)

