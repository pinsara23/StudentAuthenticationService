from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, Literal
from datetime import datetime
import re

class StudentBase(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    phone: str
    department: str = Field(..., min_length=1)
    batch: str
    semester: int = Field(..., gt=0)
    status: Literal["active", "inactive"] = "active"

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise ValueError("Invalid phone number format")
        return value

class StudentCreate(StudentBase):
    student_number: str = Field(..., min_length=1)
    email: EmailStr

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None 
    phone: Optional[str] = None
    department: Optional[str] = None
    batch: Optional[str] = None
    semester: Optional[int] = Field(None, gt=0)
    status: Optional[Literal["active", "inactive"]] = None

class StudentResponse(StudentBase):
    id: int
    student_number: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True