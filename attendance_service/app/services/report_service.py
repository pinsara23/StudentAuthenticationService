from sqlalchemy.orm import Session
from app.models.attendance_record import AttandanceRecord
from app.models.attendance_session import AttendanceSession

def get_student_summary(db: Session, student_id: int):
    records = db.query(AttandanceRecord).filter(AttandanceRecord.student_id == student_id).all()

    total = len(records)
    present = sum(1 for r in records if r.status == "PRESENT")
    absent = sum(1 for r in records if r.status == "ABSENT")
    late = sum(1 for r in records if r.status == "LATE")

    attended = present + late
    percentage = (attended / total * 100) if total > 0 else 0.0

    return{
        "student_id": student_id,
        "total_sessions": total,
        "present":present,
        "absent":absent,
        "late":late,
        "attendance_percentage": round(percentage, 2)
    }

def get_course_summary(db: Session, course_id: int):

    sessions = db.query(AttendanceSession.id).filter(AttendanceSession.course_id == course_id).all()
    session_ids = [s[0] for s in sessions]

    records = db.query(AttandanceRecord).filter(AttandanceRecord.session_id.in_(session_ids)).all()

    unique_students = len(set([r.student_id for r in records]))

    return {
        "course_id": course_id,
        "total_students": unique_students,
        "present": sum(1 for r in records if r.status == "PRESENT"),
        "absent": sum(1 for r in records if r.status == "ABSENT"),
        "late": sum(1 for r in records if r.status == "LATE")
    }