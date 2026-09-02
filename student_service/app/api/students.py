from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.connection import get_db
from app.schemas.student_schema import StudentCreate, StudentUpdate, StudentResponse
from app.services import student_service
from app.core.auth import get_current_user, RoleChecker

router = APIRouter(
    prefix="/students",
    tags = ["Students"]
)

# RBAC Dependencies

allow_admin = RoleChecker(["admin"])
allow_admin_lecturer = RoleChecker(["admin", "lecturer"])
allow_student = RoleChecker(["student"])

@router.get("/me", response_model=StudentResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user: dict = Depends(allow_student)
):
    """Student profile viewing (Requires Student role)"""
    email = current_user.get("sub")
    student = db.query(student_service.Student).filter(student_service.Student.email == email).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/search", response_model=List[StudentResponse], dependencies=[Depends(allow_admin_lecturer)])
def search_students(
    student_number: Optional[str] = None,
    department: Optional[str] = None,
    batch: Optional[str] = None,
    db: Session = Depends(get_db)
):
    "Search students (Admin & Lecturer)"
    return student_service.search_student(db, student_number=student_number, department=department, batch=batch)

@router.post("/", response_model=StudentResponse, dependencies=[Depends(allow_admin)])
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    """Create a new student (Admin only)"""
    return student_service.create_student(db, student)

@router.get("/", response_model=List[StudentResponse], dependencies=[Depends(allow_admin_lecturer)])
def get_all_students(db: Session):
    return student_service.search_student(db)  # Return all students if no filters are provided

@router.get("/{id}", response_model=StudentResponse, dependencies=[Depends(get_current_user)])
def get_student(
        student_id: int,
        db: Session = Depends(get_db)
):
    return student_service.get_student(db, student_id)

@router.put("/{id}", response_model=StudentResponse, dependencies=[Depends(allow_admin)])
def update_student(
        student_id: int,
        student: StudentUpdate,
        db: Session = Depends(get_db)
):
    return student_service.update_student(db, student_id, student)

@router.delete("/{id}", dependencies=[Depends(allow_admin)])
def delete_student(
        student_id: int,
        db: Session = Depends(get_db)
):
    return student_service.delete_student(db, student_id)