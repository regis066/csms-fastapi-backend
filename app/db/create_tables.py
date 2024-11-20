from app.db.database import engine, Base
from app.models import User,Project,VolunteerAssignment

def create_tables():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
