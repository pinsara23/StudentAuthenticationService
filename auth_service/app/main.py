from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Authentication Service", version="1.0.0")
app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"message": "Authentication Service is running."}