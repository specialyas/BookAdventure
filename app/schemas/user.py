from datetime import datetime, timezone
from typing import Optional
# from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    # username: str 
    email: EmailStr
    password: str


class UserIn(BaseModel):
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: Optional[datetime] = None


    class Config:
        from_attributes = True
