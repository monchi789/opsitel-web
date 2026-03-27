from fastapi import FastAPI

from app.modules.auth.interfaces.http.v1.router import router as auth_router
from app.modules.users.interfaces.http.v1.router import router as users_router


def register_routers(app: FastAPI) -> None:
    """Register all API routers in one place."""
    app.include_router(auth_router, prefix="/api/v1")
    app.include_router(users_router, prefix="/api/v1")

