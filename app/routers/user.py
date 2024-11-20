from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.crud.user import user_crud
from app.db.database import get_db
from uuid import UUID

router = APIRouter()


@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    return user_crud.create(db=db, obj_in=user)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    """
    Get a user by ID.
    """
    db_user = user_crud.get(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/", response_model=list[UserResponse])
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of users with pagination.
    """
    users = user_crud.get_all(db=db, skip=skip, limit=limit)
    return users


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: UUID, user: UserUpdate, db: Session = Depends(get_db)):
    """
    Update user details.
    """
    db_user = user_crud.get(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.update(db=db, db_obj=db_user, obj_in=user)


@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    """
    Delete a user by ID.
    """
    success = user_crud.delete(db=db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
