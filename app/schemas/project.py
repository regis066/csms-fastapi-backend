from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date


# Shared properties for Project
class ProjectBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str | None = Field(None, max_length=500)
    start_date: date
    end_date: date | None = None
    status: str = Field(..., max_length=50)


# Schema for creating a new project
class ProjectCreate(ProjectBase):
    pass  # All fields from ProjectBase are required for creation


# Schema for updating an existing project
class ProjectUpdate(BaseModel):
    name: str | None = Field(None, max_length=100)
    description: str | None = Field(None, max_length=500)
    start_date: date | None = None
    end_date: date | None = None
    status: str | None = Field(None, max_length=50)


# Schema for returning project details
class ProjectResponse(ProjectBase):
    id: UUID

    class Config:
        from_attributes = True
