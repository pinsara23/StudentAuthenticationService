from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.student import Student
from app.schemas.student_schema import StudentCreate, StudentUpdate


def create_student(db: Session, student_in: StudentCreate):

    if db.query(Student).filter(Student.student_number == student_in.student_number).first():
        raise HTTPException(status_code=400, detail="Student with this student number already exists")
    if db.query(Student).filter(Student.email == student_in.email).first():
        raise HTTPException(status_code=400, detail="Student with this email already exists")

    db_student = Student(**student_in.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

def search_student(db: Session, student_number: str = None, name : str = None, department: str = None, batch: str = None):
    query = db.query(Student)
    if student_number:
        query = query.filter(Student.student_number == student_number)
    if name:
        query = query.filter((Student.first_name.ilike(f"%{name}%")) | (Student.last_name.ilike(f"%{name}%")))
    if department:
        query = query.filter(Student.department == department)
    if batch:
        query = query.filter(Student.batch == batch)
    return query.all()

def update_student(db: Session, student_id: int, student_in: StudentUpdate):
    db_student = get_student(db, student_id)
    update_data = student_in.model_dump(exclude_unset=True) #update only the fields that are provided in the request

    for key, value in update_data.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    db.delete(db_student) # delete the student record from the database
    db.commit()
    return {"detail": "Student deleted successfully"}