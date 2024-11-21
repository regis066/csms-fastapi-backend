from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from uuid import UUID
from passlib.context import CryptContext
from app.core.config import settings


# Initialize password hashing context (using bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CRUDUser:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, obj_in: UserCreate) -> User:
        """Create a new user."""
        # Hash the user's password before storing it
        hashed_password = self.hash_password(obj_in.password)
        db_obj = self.model(
            username=obj_in.username,
            email=obj_in.email,
            password_hash=hashed_password,
            role=obj_in.role,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, user_id: UUID) -> User | None:
        """Get a user by ID."""
        return db.query(self.model).filter(self.model.id == user_id).first()

    def get_by_email(self, db: Session, email: str) -> User | None:
        """Get a user by email."""
        return db.query(self.model).filter(self.model.email == email).first()

    def update(self, db: Session, db_obj: User, obj_in: UserUpdate) -> User:
        """Update a user."""
        obj_data = obj_in.dict(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, user_id: UUID) -> bool:
        """Delete a user."""
        db_obj = db.query(self.model).filter(self.model.id == user_id).first()
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False

    def get_all(self, db: Session, skip: int = 0, limit: int = 10):
        """Retrieve all users with pagination."""
        return db.query(self.model).offset(skip).limit(limit).all()

    def hash_password(self, password: str) -> str:
        """Hash a password for storing in the database."""
        return pwd_context.hash(password)


user_crud = CRUDUser(User)
