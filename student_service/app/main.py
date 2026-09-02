from fastapi import FastAPI
from app.api.students import router as student_router
from app.database.connection import engine, Base

# Create tables in the local PostgreSQL database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Service",
    description="Week 2 - Student Management Microservice with RBAC",
    version="1.0.0"
)

app.include_router(student_router)

@app.get("/")
def health_check():
    return {"status": "Student Service is running"}