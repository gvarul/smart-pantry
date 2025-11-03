from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "devsecret"
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    EMAIL_FROM: str = "noreply@example.com"
    FCM_SERVER_KEY: str = ""
    CHECK_INTERVAL_MINUTES: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
