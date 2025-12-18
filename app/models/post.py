# Import column and data type definitions from SQLAlchemy
from sqlalchemy import Column, Integer, String

# Import the declarative base class for ORM models
from app.db.base import Base


# Define a SQLAlchemy ORM model for the "blog" table
class Post(Base):
    # Name of the database table
    __tablename__ = "post"

    # Primary key column (unique identifier for each blog record)
    id = Column(Integer, primary_key=True)

    # Column to store the blog title
    title = Column(String)

    # Column to store the blog content/body
    body = Column(String)
