from sqlalchemy import Column, Integer, Column, String
from app.database import Base


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)