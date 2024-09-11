from dotenv import load_dotenv
import os

load_dotenv()
USER_DB = os.getenv('POSTGRES_USER')
PWS_DB = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER_DB}:{PWS_DB}@localhost/{DB_NAME}"