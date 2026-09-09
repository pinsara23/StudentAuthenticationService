from sqlalchemy import Column, Date, Integer, String, DateTime, Time
from datetime import datetime
from app.database.connection import Base

class AttendanceSession(Base):
    __tablename__ = "attendance_sessions"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, nullable=False)
    course_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    created_by = Column(Integer, nullable=False)  # Owned by Auth Service
    created_at = Column(DateTime, default=datetime.utcnow)