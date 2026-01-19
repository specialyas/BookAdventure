from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.schemas.response import StandardResponse
from app.schemas.pagination import PaginatedResponse
from app.utils import hash
from app.utils.response import bad_request_response, success_response, not_found_response
from app.utils.pagination import paginate_and_create_response
from app.config.pagination import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, MIN_PAGE_SIZE



class UserService:

    # add a new user 
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> StandardResponse[UserResponse]:
        """create new user"""
        if not user.email or not user.email.strip():
            raise bad_request_response("Email is required")

        # hash user password 
        hashed_password = hash.getpasswordhash(user.password)
        new_user = User(
            email=user.email, 
            password=hashed_password
            )

        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            user_response = UserResponse.model_validate(new_user)
            user_dict = user_response.model_dump()
            return success_response("User created successfully", data=user_dict)
        except IntegrityError:
            db.rollback()
            raise bad_request_response("email already exist")
        
    # get all users 
    @staticmethod
    def get_all_users(
        db: Session,
        page: int = 1,
        size: int = DEFAULT_PAGE_SIZE,
        search_term:  Optional[str] = None,
    ) -> PaginatedResponse[UserResponse]:
        """get all users with pagination"""

        try:
            offset = (page - 1) * size
            query = db.query(User)
            
            if search_term:
                query = query.filter(User.email.ilike(f"%{search_term}%"))

            total = query.count()
            users = query.offset(offset).limit(size).all()

            user_responses = [UserResponse.model_validate(user) for user in users]
            user_dicts = [user.model_dump() for user in user_responses]
            return paginate_and_create_response(
            query=query,
            page=page,
            per_page=size,
            message="Categories retrieved successfully",
        )
            # return success_response(
            #     "Users retrieved successful",
            #     data={
            #         "items": user_dicts,
            #         "total": total,
            #         "page": page,
            #         "size": size
            #     }
            # )
        except Exception as e:
            raise bad_request_response(f"Error retrieving users: {str(e)}")

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> StandardResponse[UserResponse]:
        """get a user with an id"""
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            return not_found_response("user")
        
        return success_response("User retrieved successfully", user)



