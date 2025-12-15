from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[datetime] = None
