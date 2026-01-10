from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, DateTime, Integer, String, ForeignKey, func, text
from app.db.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    # username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        onupdate=func.now(),
                        server_default=func.now(),
    )