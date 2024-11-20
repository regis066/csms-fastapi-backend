from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.crud.project import project_crud
from app.db.database import get_db
from uuid import UUID

router = APIRouter()


@router.post("/projects/", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    """
    Create a new project.
    """
    return project_crud.create(db=db, obj_in=project)


@router.get("/projects/{project_id}", response_model=ProjectResponse)
def get_project(project_id: UUID, db: Session = Depends(get_db)):
    """
    Get a project by ID.
    """
    db_project = project_crud.get(db=db, project_id=project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.get("/projects/", response_model=list[ProjectResponse])
def get_all_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of all projects with pagination.
    """
    projects = project_crud.get_all(db=db, skip=skip, limit=limit)
    return projects


@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: UUID, project: ProjectUpdate, db: Session = Depends(get_db)
):
    """
    Update project details.
    """
    db_project = project_crud.get(db=db, project_id=project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project_crud.update(db=db, db_obj=db_project, obj_in=project)


@router.delete("/projects/{project_id}", response_model=dict)
def delete_project(project_id: UUID, db: Session = Depends(get_db)):
    """
    Delete a project by ID.
    """
    success = project_crud.delete(db=db, project_id=project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"detail": "Project deleted successfully"}
