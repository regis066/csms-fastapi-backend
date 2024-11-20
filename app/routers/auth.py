from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import user_crud
from app.db.database import get_db
from app.core.security import create_access_token, verify_password
from app.services.auth_service import authenticate_user

router = APIRouter()


@router.post("/register/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user (could be a volunteer or admin).
    """
    # Check if user already exists
    db_user = user_crud.get_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create(db=db, obj_in=user)


@router.post("/login/")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    """
    Login an existing user (getting a JWT token).
    """
    user = authenticate_user(db=db, email=email, password=password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
