from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services import report_service
from app.core.auth import RoleChecker, get_current_user

router = APIRouter(prefix="/reports", tags=["Reports"])

allow_all = Depends(get_current_user)
allow_admin_lecturer = RoleChecker(["admin", "lecturer"])

@router.get("/students/{student_id}", dependencies=[allow_all])
def student_attendance_summary(student_id: int, db: Session = Depends(get_db)):
    """View a student's total attendance statistics."""
    # Note: In a production app, you would verify if the student requesting this matches the student_id!
    return report_service.get_student_summary(db, student_id)

@router.get("/courses/{course_id}", dependencies=[Depends(allow_admin_lecturer)])
def course_attendance_summary(course_id: int, db: Session = Depends(get_db)):
    """Admin/Lecturer: View statistics for an entire course."""
    return report_service.get_course_summary(db, course_id)