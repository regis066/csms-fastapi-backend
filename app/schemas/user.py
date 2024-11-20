from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    volunteer = "volunteer"


class UserBase(BaseModel):
    username:str = Field(..., max_length=50)
    email: EmailStr
    role: UserRole


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    username: str | None = Field(None, max_length=50)
    email: EmailStr | None = None
    role: UserRole | None = None
    password: str | None = Field(None, min_length=8)

class UserResponse(UserBase):
    id: UUID

    class Config:
        from_attributes = True
