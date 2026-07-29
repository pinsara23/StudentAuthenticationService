from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
autocommit=False : SQLALChemy does not save automatically my changes 
user = User(name="John")
db.add(user)

after this have to perform 
db.commit() - to save the changes in the database

autoflush=False : Flushing means SQLAlchemy sends pending SQL statements to the database without committing them.
user = User(name="Alice")
db.add(user)

At this point:

Python knows about the new user.
The database does not yet.

"""
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

