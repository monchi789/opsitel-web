from fastapi import APIRouter, Depends, Response, status
from fastapi_filter import FilterDepends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app.modules.users.application.dto import User, UserCreate, UserUpdate
from app.modules.users.application.use_cases import (
    create_user,
    eliminate_user,
    list_user,
    list_user_by_id,
    partial_update_user,
)
from app.modules.users.interfaces.http.v1.filters import UserFilter
from app.shared.interfaces.http.deps import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/", response_model=Page[User])
def get_users(
    db: Session = Depends(get_db),
    user_filter: UserFilter = FilterDepends(UserFilter),
):
    return paginate(list_user(db, user_filter))


@router.get("/{id}", response_model=User)
def get_user(id: str, db: Session = Depends(get_db)):
    return list_user_by_id(db, id)


@router.patch("/{id}", response_model=User)
def patch_user(id: str, user: UserUpdate, db: Session = Depends(get_db)):
    return partial_update_user(db, id, user)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: str, db: Session = Depends(get_db)):
    eliminate_user(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

