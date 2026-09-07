from pydantic import BaseModel, Field
from datetime import datetime

class CourseCreate(BaseModel):

    course_code: str = Field(..., min_length=2)
    course_name: str = Field(..., min_length=2)
    lecturer_id: int

class CourseResponse(CourseCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True