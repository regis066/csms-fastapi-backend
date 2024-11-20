from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid
from enum import Enum as PyEnum


class UserRole(PyEnum):
    admin = "admin"
    volunteer = "volunteer"


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(Enum(UserRole), default=UserRole.volunteer)

    assignments = relationship("VolunteerAssignment", back_populates="volunteer")
