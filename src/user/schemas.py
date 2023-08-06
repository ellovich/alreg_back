import enum
from typing import Optional

from fastapi_users import schemas
from pydantic import ConfigDict, EmailStr
from sqlalchemy import Enum, String

# class SRoleEnum(Enum(String)):
#     user = "user"
#     admin = "admin"


class SUserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    model_config = ConfigDict(from_attributes=True)  # type: ignore


class SUserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    doctor_id: Optional[int]
    role_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)  # type: ignore


class SUserUpdate(schemas.BaseUserUpdate):

    model_config = ConfigDict(from_attributes=True)  # type: ignore