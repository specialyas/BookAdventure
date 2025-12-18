# Import the function used to create a database engine (connection manager)
from sqlalchemy import create_engine

# Import tools for creating database sessions and ORM model base classes
from sqlalchemy.orm import sessionmaker

# Import application settings (contains database connection string)
from app.core.config import settings


# Create the SQLAlchemy engine using the database connection string
# This engine manages connections and communicates with the database
engine = create_engine(
    settings.sqlalchemy_string
)


# Create a configured session factory
# - autocommit=False: transactions must be committed manually
# - autoflush=False: changes are not automatically written to the DB before queries
# - bind=engine: sessions will use the engine created above
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

