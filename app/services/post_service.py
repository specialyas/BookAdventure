from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
# from app.api import dep
from app.config.pagination import DEFAULT_PAGE_SIZE
from app.models.post import Post
from app.schemas.pagination import PaginatedResponse
from app.schemas.post import PostResponse
from app.utils.pagination import paginate_and_create_response
from app.utils.response import bad_request_response






# def create_post(db: Session, post_title: str, post_body: str) -> Post:
#     """add a new blog"""
#     new_post = Post(title=post_title, body=post_body )
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post

class PostService:

    def get_all_posts(
            db: Session,
            page: int = 1,
            size: int = DEFAULT_PAGE_SIZE,
            search_term: Optional[str] = None
    )-> PaginatedResponse[PostResponse]:
        """get all posts with pagination"""
        try:
            offset = (page - 1) * size
            query = db.query(Post)
            
            if search_term:
                query = query.filter(Post.title.ilike(f"%{search_term}%"))

            total = query.count()
            posts = query.offset(offset).limit(size).all()

            return paginate_and_create_response(
            query=query,
            page=page,
            per_page=size,
            message="Categories retrieved successfully",
        )
        except Exception as e:
            raise bad_request_response(f"Error retrieving users: {str(e)}")



        

# def fetch_posts(db: Session ):
#     """get all blog post"""
#     post = db.query(Post).all()
#     if not post:
#         return {"data": "no post has been found"}
#     return post


# def fetch_post_by_id(post_id, db: Session):
#     """fetch post by id """
#     post = db.get(Post, post_id)
#     # print(post)
#     if not post:
#         raise HTTPException(status_code=404, detail=f"Blog with id ({id}) not found")

#     return post


# def delete_post(post_id, db: Session):
#     """delete post"""
#     post = db.get(Post, post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail=f"Blog with id ({post_id}) not found")
#     db.delete(post)
#     db.commit()
#     return "post delete success"




# def update_post(post_id: int, db: Session, post_title: str, post_body: str) -> Post:
#     """update post """
#     post = db.get(Post, post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail=f"Blog with id ({post_id}) not found")
#     post.title = post_title
#     post.body = post_body
#     db.commit()
#     db.refresh(post)
#     return post
# #
