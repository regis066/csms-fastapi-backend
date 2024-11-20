# app/services/user_service.py

from app.crud import user as user_crud
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int) -> UserResponse:
    """Get a user by ID."""
    db_user = user_crud.get(db=db, item_id=user_id)
    return UserResponse.from_orm(db_user)


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> UserResponse:
    """Update a user's details."""
    db_user = user_crud.update(db=db, item_id=user_id, item_data=user_update.dict())
    return UserResponse.from_orm(db_user)
