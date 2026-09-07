from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.connection import Base

class AttandanceRecord(Base):
    __tablename__ = "attendance_records"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)  # Owned by Student Service
    status = Column(String, nullable=False)       # PRESENT, ABSENT, or LATE
    marked_at = Column(DateTime, default=datetime.utcnow)
    marked_by = Column(Integer, nullable=False)   # Owned by Auth_Service