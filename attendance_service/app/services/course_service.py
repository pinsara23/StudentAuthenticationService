from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.course import Course
from app.schemas.course_sehema import CourseCreate

def create_course(db: Session, course_in:CourseCreate):

    existing = db.query(Course).filter(Course.course_code == course_in.course_code).first()
    if existing:
        raise HTTPException(status_code=409, detail="Course with this code already exists")

    db_course = Course(**course_in.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

def get_all_course(db: Session):
    return db.query(Course).all()