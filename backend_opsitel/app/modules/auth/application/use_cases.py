from fastapi import HTTPException, status

from app.modules.auth.application.dto import TokenResponse, RefreshToken
from app.modules.users.application.use_cases import authenticate_user
from app.shared.infrastructure.security import create_access_token, create_refresh_token


def get_token(db, email: str, password: str) -> TokenResponse:
    user = authenticate_user(db, email, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    return TokenResponse(access_token=access_token, refresh_token=refresh_token, token_type="bearer")


def get_refresh_token(db, email: str, password: str) -> RefreshToken:
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token = create_refresh_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    return RefreshToken(access_token=access_token, refresh_token=refresh_token)

