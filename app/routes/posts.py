from typing import List
from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostOut
from app.api.deps import get_db
from app.services.post_service import create_post, fetch_posts, fetch_post_by_id, delete_post, update_post


router = APIRouter(

    prefix="/posts", 
    tags=["posts"]
)


# create post
@router.post("/", response_model=PostCreate)
def create_blog(post: PostCreate, db: Session = Depends(get_db)):
    """add a new blog"""
    return create_post(db, post.title, post.body)

# get post
@router.get("/", response_model=List[PostOut])
def get_posts(db: Session = Depends(get_db)):
    """get all blog post"""
    return fetch_posts(db)

# get post by id
@router.get("/{post_id}", response_model=PostOut)
def get_post_by_id(post_id, db: Session = Depends(get_db)):
    """get a post by id"""
    return fetch_post_by_id(post_id, db)

# delete post
@router.delete("/")
def delete_posts(post_id, db: Session = Depends(get_db)):
    """get all blog post"""
    return delete_post(post_id, db)


@router.put("/{post_id}", response_model=PostCreate)
def edit_post( post_id: int, post: PostCreate,  db: Session = Depends(get_db)):
    """update post using the id"""
    return update_post(post_id, db, post.title, post.body)

