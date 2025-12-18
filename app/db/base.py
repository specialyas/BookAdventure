from sqlalchemy.orm import  declarative_base


# Create a base class for all ORM models
# All database models should inherit from this class
Base = declarative_base()
