from pydantic import BaseModel, EmailStr, Field # thid is dto
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=4)
    role: str = "student"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str 

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str 

class TokenVerificationResponse(BaseModel):
    is_valid: bool
    user_id: Optional[int] = None
    role: Optional[str] = None
