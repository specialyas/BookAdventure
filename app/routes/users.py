from typing import List, Optional
from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session
from app.schemas.response import StandardResponse
from app.schemas.user import  UserIn, UserCreate, UserResponse
from app.schemas.pagination import PaginatedResponse
from app.api.deps import get_db
from app.services.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

""" 
def add_user(
    ): """

@router.post(
        '/', 
        response_model=StandardResponse[UserResponse],
        summary="create a new user",
        description="creates a new user with the information provided",
        status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """create a new user"""
    return UserService.create_user(db, user)



@router.get("/",
        response_model=PaginatedResponse[UserResponse],
        summary="get all users",
        description="returns all the users in the database"
)
def get_users(
    db: Session = Depends(get_db),
    page: int = 1,
    size: int = 10,
    search: Optional[str] = None,
):
    """"fetch all users"""
    return UserService.get_all_users(db, page, size, search)


@router.get(
        "/{user_id}",
        response_model=StandardResponse[UserResponse],
        summary="get a user with a specific id",
        description="returns a specific user using the id"
        )
def get_users_by_id(user_id: int, db: Session = Depends(get_db)):
    """"fetch user with a specific id"""
    return UserService.get_user_by_id( db, user_id)

""" 
@router.get(
    "/{category_id}",
    response_model=StandardResponse[CategoryResponse],
    summary="Get category by ID",
    description="Returns a specific category by its ID.",
)
async def get_category(category_id: str, db: Session = Depends(get_db)):
    Get a specific category by ID.
    return CategoryService.get_category_by_id(category_id, db)

 """