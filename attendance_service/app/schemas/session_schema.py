from pydantic import BaseModel, Field
from datetime import datetime, time, date

class SessionCreate(BaseModel):

    course_id: int
    date: date
    start_time: time
    end_time: time
    #created by is extracted from JWT

class SessionResponse(SessionCreate):
    id: int
    crated_by: int
    created_at: datetime

    class Config:
        from_attributes = True
    