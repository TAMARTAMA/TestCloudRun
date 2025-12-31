from dotenv import load_dotenv
import os
import ast

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv("app/.env")

APP_NAME = os.getenv("APP_NAME", "Dovaiv")
VERSION = os.getenv("VERSION", "0.1.0")

PORT = int(os.getenv("PORT", 8000))  
CORS_ORIGINS = ast.literal_eval(os.getenv("CORS_ORIGINS", "[]"))  

API_PREFIX = os.getenv("API_PREFIX", "/prod")


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
import os

print("DB_PORT raw =", os.getenv("DB_PORT"))
print("DB_HOST raw =", os.getenv("DB_HOST"))

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


API_KEY = os.getenv("API_KEY")
print(f"🚀🚀 The server run on port: {PORT} with cors origins: {CORS_ORIGINS}")
