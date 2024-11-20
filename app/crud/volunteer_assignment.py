from sqlalchemy.orm import Session
from app.models.volunteer_assignment import VolunteerAssignment
from app.schemas.volunteer_assignment import (
    VolunteerAssignmentCreate,
    VolunteerAssignmentUpdate,
)
from uuid import UUID


class CRUDVolunteerAssignment:
    def __init__(self, model):
        self.model = model

    def create(
        self, db: Session, obj_in: VolunteerAssignmentCreate
    ) -> VolunteerAssignment:
        """Create a new volunteer assignment."""
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, assignment_id: UUID) -> VolunteerAssignment | None:
        """Get a volunteer assignment by ID."""
        return db.query(self.model).filter(self.model.id == assignment_id).first()

    def update(
        self,
        db: Session,
        db_obj: VolunteerAssignment,
        obj_in: VolunteerAssignmentUpdate,
    ) -> VolunteerAssignment:
        """Update a volunteer assignment."""
        obj_data = obj_in.dict(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, assignment_id: UUID) -> bool:
        """Delete a volunteer assignment."""
        db_obj = db.query(self.model).filter(self.model.id == assignment_id).first()
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False

    def get_all(self, db: Session, skip: int = 0, limit: int = 10):
        """Retrieve all volunteer assignments with pagination."""
        return db.query(self.model).offset(skip).limit(limit).all()


# Initialize CRUD instance
volunteer_assignment_crud = CRUDVolunteerAssignment(VolunteerAssignment)
