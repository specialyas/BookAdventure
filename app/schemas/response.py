from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class StandardResponse(BaseModel, Generic[T]):

    success: bool
    message: str
    data: T | None = None

    class Config:
        from_attributes = True

