from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.modules.auth.application.dto import TokenResponse, RefreshToken
from app.modules.auth.application.use_cases import get_token
from app.shared.interfaces.http.deps import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def get_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return get_token(db, form_data.username, form_data.password)


@router.post("/refresh", response_model=RefreshToken)
def get_refresh_token():
    pass