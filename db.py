from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database URL. The database file will be named "catalog.db"
# in the same directory.
SQLALCHEMY_DATABASE_URL = "sqlite:///./catalog.db"

# Create the SQLAlchemy engine.
# connect_args is needed only for SQLite to allow multi-threaded access.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class. Each instance of SessionLocal will be a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class. Our ORM models will inherit from this class.
Base = declarative_base()

# Dependency to get a DB session. This will be used in our path operations.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()