import os
from pydantic import BaseModel


class Settings(BaseModel):
    """
    Application settings, loaded from environment variables.
    """
    # API Configuration:
    appName: str = "Person API"
    debug: bool = bool(os.getenv("DEBUG", True))
    ## These two variables are for the APITester only
    apiExternalServer: str = os.getenv("API_SERVER", "localhost")
    apiExternalPort: str = str(os.getenv("API_PORTT", 8000))

    # DB Configuration:
    hostname: str = os.getenv("DB_HOST", "localhost")
    psqlUser: str = os.getenv("DB_USER", "postgres")
    psqlPassword: str = os.getenv("DB_PASSWORD", "admin")
    databaseName: str = os.getenv("DB_NAME", "person_db")

    database_url: str = f"postgresql://{psqlUser}:{psqlPassword}@{hostname}:5432/{databaseName}"

settings = Settings()
