from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.session_schema import SessionCreate, SessionResponse
from app.schemas.attendance_schema import RecordCreate, RecordResponse
from app.services import attendance_service
from app.core.auth import RoleChecker

router = APIRouter(prefix="/attendance", tags=["Attendance"])

allow_admin_lecturer = RoleChecker(["admin", "lecturer"])

@router.post("/sessions", response_model=SessionResponse)
def create_session(
    session: SessionCreate, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(allow_admin_lecturer)
):
    """Admin/Lecturer: Create a session (Ownership checked in service)."""
    return attendance_service.create_session(db, session, current_user["user_id"], current_user["role"])

@router.post("/sessions/{session_id}/records", response_model=RecordResponse)
async def mark_attendance(
    session_id: int,
    record: RecordCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(allow_admin_lecturer)
):
    """Admin/Lecturer: Mark student attendance (Calls Student Service)."""
    return await attendance_service.create_record(
        db=db, 
        session_id=session_id, 
        record_in=record, 
        user_id=current_user["user_id"], 
        role=current_user["role"], 
        token=current_user["raw_token"]
    )