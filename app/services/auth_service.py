# app/services/auth_service.py

from app.crud.user import user_crud
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password, verify_password
from sqlalchemy.orm import Session


def create_user(db: Session, user: UserCreate) -> UserResponse:
    """Create a new user."""
    hashed_password = hash_password(user.password)
    db_user = user_crud.create(
        db=db, user_data={**user.dict(), "password": hashed_password}
    )
    return UserResponse.from_orm(db_user)


def authenticate_user(db: Session, email: str, password: str) -> User:
    """Authenticate a user with email and password."""
    user = user_crud.get_by_email(db, email=email)
    if user and verify_password(password, user.password_hash):
        return user
    return None
