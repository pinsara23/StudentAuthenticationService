from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.course import Course
from app.models.attendance_session import AttendanceSession
from app.models.attendance_record import AttandanceRecord
from app.schemas.session_schema import SessionCreate
from app.schemas.attendance_schema import RecordCreate
from app.clients.student_client import verify_student_exists

def create_session(db: Session, session_in: SessionCreate, user_id: int, role: str):

    #verify course exists
    course = db.query(Course).filter(Course.id == session_in.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    #ownership check
    if role == "lecturer" and course.lecturer_id != user_id:
        raise HTTPException(status_code=403, detail="You do not have permission to create a session for this course")

    db._session = AttendanceSession(**session_in.model_dump(), created_by=user_id)
    db.add(db._session)
    db.commit()
    db.refresh(db._session)
    return db._session

async def create_record(db: Session, record_in: RecordCreate, session_id: int, user_id: int, role: str, token: str):
    #verify session exists
    session = db.query(AttendanceSession).filter(AttendanceSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    #ownership check
    if role == "lecturer" :
        course = db.query(Course).filter(Course.id == session.course_id).first()
        if course.lecturer_id != user_id:
            raise HTTPException(status_code=403, detail="You do not have permission to create a record for this session")

    #duplicate check
    existing_record = db.query(AttandanceRecord).filter(
        AttandanceRecord.session_id == session_id, 
        AttandanceRecord.student_id == record_in.student_id).first()
    if existing_record:
        raise HTTPException(status_code=409, detail="Record already exists for this student in this session")

    #inter service communication to verify student exists
    await verify_student_exists(record_in.student_id, token)

    db_record = AttandanceRecord(**record_in.model_dump(), session_id=session_id, marked_by=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record