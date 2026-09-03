from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from app.model.user import User # this is for db processes like entity
from app.schemas.user_schema import UserCreate, LoginRequest
from app.core.config import config
from app.core.security import hash_password, verify_passwords, create_access_token
from app.database.connection import get_db

security = HTTPBearer()

def register_user(db: Session, user_data: UserCreate):

    #check user is already registered or not
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    hashed_password = hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, login_data: LoginRequest):

    #get user from database based on email and verify password
    user = db.query(User).filter(User.email == login_data.email).first()

    if not user or not verify_passwords(login_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid email or password",
                            headers={"WWW-Authenticate": "Bearer"})
    return user

def create_token_for_user(user: User):
    access_token = create_access_token(data={"sub": user.email, "user_id": user.id, "role": user.role})
    return access_token

def get_current_user(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)):

    try:
        payload = jwt.decode(credentials.credentials, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def verify_token(token: str):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        user_id = payload.get("user_id")
        role = payload.get("role")
        if user_id is None:
            return {"valid": False}
        return {"valid": True, "user_id": user_id, "role": role}
    except JWTError:
        return {"valid": False}









