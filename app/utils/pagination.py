"""
Pagination utility functions for standardized pagination across all list endpoints
"""

import math
from typing import Any, List, TypeVar

from sqlalchemy.orm import Query
from sqlalchemy.sql import func

from app.config.pagination import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, MIN_PAGE_SIZE
from app.schemas.pagination import Meta, PaginatedData, PaginatedResponse

T = TypeVar("T")


def calculate_pagination_meta(
    total_items: int, current_page: int, per_page: int
) -> Meta:
    """
    Calculate pagination metadata

    Args:
        total_items: Total number of items across all pages
        current_page: Current page number (1-based)
        per_page: Number of items per page

    Returns:
        Meta object with calculated pagination information
    """
    total_pages = math.ceil(total_items / per_page) if total_items > 0 else 1

    # Ensure current_page doesn't exceed total_pages
    current_page = min(current_page, total_pages)

    has_next = current_page < total_pages
    has_previous = current_page > 1

    next_page = current_page + 1 if has_next else None
    previous_page = current_page - 1 if has_previous else None

    return Meta(
        total_pages=total_pages,
        current_page=current_page,
        next_page=next_page,
        previous_page=previous_page,
        per_page=per_page,
        total_items=total_items,
        has_next=has_next,
        has_previous=has_previous,
    )


def paginate_query(
    query: Query, page: int = 1, per_page: int = DEFAULT_PAGE_SIZE
) -> tuple[List[Any], int]:
    """
    Paginate a SQLAlchemy query

    Args:
        query: SQLAlchemy query object
        page: Page number (1-based)
        per_page: Number of items per page

    Returns:
        Tuple of (items, total_count)
    """
    # Calculate offset
    offset = (page - 1) * per_page

    # Get total count
    total_count = query.count()

    # Apply pagination
    items = query.offset(offset).limit(per_page).all()

    return items, total_count


def create_paginated_response(
    items: List[T],
    total_items: int,
    current_page: int,
    per_page: int,
    message: str = "Data retrieved successfully",
) -> PaginatedResponse[T]:
    """
    Create a standardized paginated response

    Args:
        items: List of items for current page
        total_items: Total number of items across all pages
        current_page: Current page number (1-based)
        per_page: Number of items per page
        message: Success message

    Returns:
        PaginatedResponse with standardized format
    """
    pagination_meta = calculate_pagination_meta(total_items, current_page, per_page)

    paginated_data = PaginatedData(data=items, meta=pagination_meta)

    return PaginatedResponse(success=True, message=message, data=paginated_data)


def paginate_and_create_response(
    query: Query,
    page: int = 1,
    per_page: int = DEFAULT_PAGE_SIZE,
    message: str = "Data retrieved successfully",
) -> PaginatedResponse[T]:
    """
    Paginate a query and create a standardized response in one step

    Args:
        query: SQLAlchemy query object
        page: Page number (1-based)
        per_page: Number of items per page
        message: Success message

    Returns:
        PaginatedResponse with standardized format
    """
    items, total_count = paginate_query(query, page, per_page)
    return create_paginated_response(items, total_count, page, per_page, message)


def get_pagination_query_params():
    """
    Get standardized pagination query parameters for FastAPI endpoints

    Returns:
        Tuple of (page, per_page) Query parameters with global defaults
    """
    from fastapi import Query

    return (
        Query(1, ge=1, description="Page number (1-based)"),
        Query(
            DEFAULT_PAGE_SIZE,
            ge=MIN_PAGE_SIZE,
            le=MAX_PAGE_SIZE,
            description=f"Number of items per page (max {MAX_PAGE_SIZE})",
        ),
    )
