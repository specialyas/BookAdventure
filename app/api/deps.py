# Import the SQLAlchemy session factory
from app.db.session import SessionLocal


# Dependency function that provides a database session
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to the caller (e.g., a FastAPI route)
        yield db
    finally:
        # Always close the session after use, even if an error occurs
        db.close()
