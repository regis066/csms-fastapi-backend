from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid


class Project(Base):
    __tablename__ = "projects"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    status = Column(String, default="active")

    assignments = relationship("VolunteerAssignment", back_populates="project")
