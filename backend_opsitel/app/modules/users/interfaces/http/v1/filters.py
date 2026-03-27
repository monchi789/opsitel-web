from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from app.modules.users.infrastructure.orm_models import User


class UserFilter(Filter):
    name__ilike: Optional[str] = None
    last_name__ilike: Optional[str] = None
    email__ilike: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[str] = None

    class Constants(Filter.Constants):
        model = User

    class config:
        populate_by_name = True

