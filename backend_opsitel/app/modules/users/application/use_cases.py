from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import cast

from app.modules.users.infrastructure.orm_models import User
from app.modules.users.application.dto import UserCreate, UserUpdate
from app.shared.infrastructure.security import get_password_hash, verify_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    hashed_password = cast(str, getattr(user, "password"))
    if not verify_password(password, hashed_password):
        return False
    return user


def create_user(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    hashed_password = get_password_hash(user.password)

    db_user = User(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
        role=user.role,
        is_active=str(user.is_active).lower(),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def list_user(db: Session, filters):
    query = db.query(User)
    query = filters.filter(query)
    return query


def list_user_by_id(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


def partial_update_user(db: Session, user_id: str, user_update: UserUpdate):
    db_user = list_user_by_id(db, user_id)

    updated_data = user_update.model_dump(exclude_unset=True)

    if "password" in updated_data:
        updated_data["password"] = get_password_hash(updated_data["password"])

    for key, value in updated_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def eliminate_user(db: Session, user_id: str):
    db_user = list_user_by_id(db, user_id)
    db.delete(db_user)
    db.commit()

