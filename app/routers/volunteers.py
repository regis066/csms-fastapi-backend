from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.volunteer_assignment import (
    VolunteerAssignmentCreate,
    VolunteerAssignmentResponse,
)
from app.crud.volunteer_assignment import volunteer_assignment_crud
from app.db.database import get_db
from uuid import UUID

router = APIRouter()


@router.post("/volunteer-assignments/", response_model=VolunteerAssignmentResponse)
def create_assignment(
    assignment: VolunteerAssignmentCreate, db: Session = Depends(get_db)
):
    """
    Create a new volunteer assignment.
    """
    return volunteer_assignment_crud.create(db=db, obj_in=assignment)


@router.get(
    "/volunteer-assignments/{assignment_id}", response_model=VolunteerAssignmentResponse
)
def get_assignment(assignment_id: UUID, db: Session = Depends(get_db)):
    """
    Get a volunteer assignment by ID.
    """
    db_assignment = volunteer_assignment_crud.get(db=db, assignment_id=assignment_id)
    if not db_assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return db_assignment


@router.get("/volunteer-assignments/", response_model=list[VolunteerAssignmentResponse])
def get_all_assignments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of all volunteer assignments with pagination.
    """
    assignments = volunteer_assignment_crud.get_all(db=db, skip=skip, limit=limit)
    return assignments


@router.put(
    "/volunteer-assignments/{assignment_id}", response_model=VolunteerAssignmentResponse
)
def update_assignment(
    assignment_id: UUID,
    assignment: VolunteerAssignmentCreate,
    db: Session = Depends(get_db),
):
    """
    Update a volunteer assignment.
    """
    db_assignment = volunteer_assignment_crud.get(db=db, assignment_id=assignment_id)
    if not db_assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return volunteer_assignment_crud.update(
        db=db, db_obj=db_assignment, obj_in=assignment
    )


@router.delete("/volunteer-assignments/{assignment_id}", response_model=dict)
def delete_assignment(assignment_id: UUID, db: Session = Depends(get_db)):
    """
    Delete a volunteer assignment by ID.
    """
    success = volunteer_assignment_crud.delete(db=db, assignment_id=assignment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return {"detail": "Assignment deleted successfully"}
