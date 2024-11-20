from fastapi import FastAPI
from app.routers import user, auth, project, volunteers
from app.db.database import engine
from app.models import (
    user as user_model,
    project as project_model,
    volunteer_assignment as volunteer_model,
)

# Initialize the FastAPI app
app = FastAPI()

# Include the routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(volunteers.router, prefix="/volunteers", tags=["volunteers"])
