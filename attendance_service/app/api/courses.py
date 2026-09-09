from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.course_sehema import CourseCreate, CourseResponse
from app.services import course_service
from app.core.auth import RoleChecker, get_current_user

router = APIRouter(prefix="/courses", tags=["Courses"])

allow_admin = RoleChecker(["admin"])
allow_all = Depends(get_current_user) # Admin, Lecturer, and Student

@router.post("/", response_model=CourseResponse, dependencies=[Depends(allow_admin)])
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Admin only: Create a new course."""
    return course_service.create_course(db, course)

@router.get("/", response_model=List[CourseResponse], dependencies=[allow_all])
def get_courses(db: Session = Depends(get_db)):
    """All authenticated users: View available courses."""
    return course_service.get_all_courses(db)

@router.get("/{course_id}", response_model=CourseResponse, dependencies=[allow_all])
def get_course(course_id: int, db: Session = Depends(get_db)):
    """All authenticated users: View a specific course."""
    return course_service.get_course(db, course_id)