# Import datetime utilities for timestamps and timezone support
from datetime import datetime, timezone

# Import Optional type hint for nullable fields
from typing import Optional

# Import BaseModel for creating Pydantic data models
from pydantic import BaseModel


# Define a Pydantic model representing a blog post
class PostCreate(BaseModel):
    title: str
    body: str
    published_at: Optional[datetime] = datetime.now(timezone.utc)


class  PostOut(BaseModel):
    id: int
    title: str
    body: str
    # user_id: int

    class Config:
        form_attributes = True
