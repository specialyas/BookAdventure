# Paginated shemaa for standardized paginated accross all list endpoints 

from typing import Any, Generic, List, Optional, TypeVar
from pydantic import BaseModel, Field
from app.config.pagination import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, MIN_PAGE_SIZE

T = TypeVar("T")


class Meta(BaseModel):
    """Pagination matedata information"""
    total_pages: int = Field(..., description="Total number of pages")
    current_page: int = Field(..., description="Current page number (1-based)")
    next_page: Optional[int] = Field(None, description="Next page number, null if no next page")
    previous_page: Optional[int] = Field(None, description="Previous page number, null if no previous page")
    per_page: int = Field(..., description="Number of items per page")
    total_items: int = Field(..., description="Total number of items across all pages")
    has_next: bool = Field(..., description="Whether there is a next page")
    has_previous: bool = Field(..., description="Whether there is a previous page")


class PaginatedData(BaseModel, Generic[T]):
    """Paginated data structure"""
    data: List[T] = Field(..., description="List of data for current page")
    meta: Meta = Field(..., description="Paginated metadata")


class PaginatedResponse(BaseModel, Generic[T]):
    """Standard paginated response that integrated with StandardResponse format"""
    success: bool = Field(True, description="Wether the operation was successful")
    message: str = Field(..., description="Response message")
    data: PaginatedData[T] = Field(..., description="Paginated data")

    class Config:
        from_attributed = True