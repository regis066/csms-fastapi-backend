# app/services/project_service.py

from app.crud import project as project_crud
from app.schemas.project import ProjectCreate, ProjectResponse
from sqlalchemy.orm import Session


def create_project(db: Session, project: ProjectCreate) -> ProjectResponse:
    """Create a new project."""
    # Use CRUD to create the project in the database
    db_project = project_crud.create(db=db, project_data=project.dict())
    # Return the project as a response
    return ProjectResponse.from_orm(db_project)


def get_project(db: Session, project_id: int) -> ProjectResponse:
    """Get a project by its ID."""
    # Use CRUD to retrieve the project from the database
    db_project = project_crud.get(db=db, item_id=project_id)
    # Return the project as a response
    return ProjectResponse.from_orm(db_project)


def update_project(
    db: Session, project_id: int, project_update: ProjectCreate
) -> ProjectResponse:
    """Update a project's details."""
    # Use CRUD to update the project in the database
    db_project = project_crud.update(
        db=db, item_id=project_id, item_data=project_update.dict()
    )
    # Return the updated project as a response
    return ProjectResponse.from_orm(db_project)


def delete_project(db: Session, project_id: int) -> None:
    """Delete a project by its ID."""
    # Use CRUD to delete the project from the database
    project_crud.delete(db=db, item_id=project_id)
