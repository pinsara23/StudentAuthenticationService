from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.connection import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String, unique=True, index=True, nullable=False)
    course_name = Column(String, nullable=False)
    lecturer_id = Column(Integer, nullable=False)     #auth_service will provide the lecturer_id
    created_at = Column(DateTime, default=datetime.utcnow)

    