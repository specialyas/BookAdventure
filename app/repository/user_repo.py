# legacy code 

from sqlalchemy.orm import Session

from app.models.user import User

class UserRepository:
    def __init__(self, db: Session ):
        self.db = db 


    def get_by_id(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)
    
    def get_all(self) -> list[User]:
        return self.db.query(User).all()
    
    def delete(self, user: User)-> None:
        self.db.delete(user)

    def save(self, user: User) -> User:
        self.db.add(user)
        return user
