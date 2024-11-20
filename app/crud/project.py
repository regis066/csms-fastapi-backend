from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from uuid import UUID


class CRUDProject:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, obj_in: ProjectCreate) -> Project:
        """Create a new project."""
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, project_id: UUID) -> Project | None:
        """Get a project by ID."""
        return db.query(self.model).filter(self.model.id == project_id).first()

    def update(self, db: Session, db_obj: Project, obj_in: ProjectUpdate) -> Project:
        """Update a project."""
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, project_id: UUID) -> bool:
        """Delete a project."""
        db_obj = db.query(self.model).filter(self.model.id == project_id).first()
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False

    def get_all(self, db: Session, skip: int = 0, limit: int = 10):
        """Retrieve all projects with pagination."""
        return db.query(self.model).offset(skip).limit(limit).all()


# Initialize CRUD instance
project_crud = CRUDProject(Project)
