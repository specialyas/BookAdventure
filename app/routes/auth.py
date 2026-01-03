from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session 
from app.api.deps import get_db
from schemas.auth import UserLogin
from app.models.user import User




router = APIRouter(tags=['Authentication'])


@router.post('login')
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    pass

