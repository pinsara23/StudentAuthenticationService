from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.user_schema import UserCreate, UserResponse, LoginRequest, TokenResponse, TokenVerificationResponse
from app.services import auth_service
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

class TokenRequest(BaseModel):
    token: str

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = auth_service.register_user(db, user_data)
    return new_user

@router.post("/login", response_model=TokenResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, login_data)
    access_token = auth_service.create_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/profile", response_model=UserResponse)
def get_profile(user: UserResponse = Depends(auth_service.get_current_user)):
    return user