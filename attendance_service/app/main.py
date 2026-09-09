from fastapi import FastAPI
from app.api.courses import router as course_router
from app.api.attendance import router as attendance_router
from app.api.report import router as report_router
from app.database.connection import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Attendance Service",
    description="Week 3 - Attendance Management and Orchestration",
    version="1.0.0"
)

app.include_router(course_router)
app.include_router(attendance_router)
app.include_router(report_router)

@app.get("/")
def health_check():
    return {"status": "Attendance Service is running on Port 8003"}