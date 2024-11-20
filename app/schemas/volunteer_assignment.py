from pydantic import BaseModel, Field
from uuid import UUID


# Shared properties for VolunteerAssignment
class VolunteerAssignmentBase(BaseModel):
    project_id: UUID
    volunteer_id: UUID
    hours_logged: int = Field(default=0, ge=0)  # Ensure non-negative values


# Schema for creating a new volunteer assignment
class VolunteerAssignmentCreate(VolunteerAssignmentBase):
    pass  # All fields are required for creation


# Schema for updating an existing assignment
class VolunteerAssignmentUpdate(BaseModel):
    project_id: UUID | None = None
    volunteer_id: UUID | None = None
    hours_logged: int | None = Field(
        None, ge=0
    )  # Optional update, must remain non-negative


# Schema for returning assignment details
class VolunteerAssignmentResponse(VolunteerAssignmentBase):
    id: UUID

    class Config:
        from_attributes = True
