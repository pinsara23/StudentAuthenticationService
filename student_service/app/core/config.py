import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    #point the auth service microservice to the student service microservice
    AUTH_SERVICE_URL: str = os.getenv("AUTH_SERVICE_URL")

settings = Settings()