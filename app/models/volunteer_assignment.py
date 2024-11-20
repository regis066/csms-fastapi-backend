from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid


class VolunteerAssignment(Base):
    __tablename__ = "volunteer_assignments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    volunteer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    hours_logged = Column(Integer, default=0)

    project = relationship("Project", back_populates="assignments")
    volunteer = relationship("User", back_populates="assignments")
