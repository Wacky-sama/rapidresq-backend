from pydantic import BaseModel, EmailStr
from app.models.user import UserRole
from typing import Optional
from uuid import UUID

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Used for creating/registering a user
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    middle_initial: Optional[str] = None
    role: UserRole

# Used for returning user info (without password)
class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    middle_initial: Optional[str] = None
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True

# JWT Token response
class Token(BaseModel):
    access_token: str
    token_type: str
