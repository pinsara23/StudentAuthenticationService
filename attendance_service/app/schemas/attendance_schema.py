from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

AttandanceStatus = Literal["PRESENT", "ABSENT", "LATE"]

class RecordCreate(BaseModel):

    student_id: int
    status: AttandanceStatus

class RecordUpdate(BaseModel):
    status: AttandanceStatus

class RecordResponse(RecordCreate):
    id: int
    session_id: int
    marked_at: datetime
    marked_by: int

    class Config:
        from_attributes = True