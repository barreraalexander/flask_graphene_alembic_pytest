from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings

POSTGRES_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
SQLITE_DATABASE_URL = 'sqlite:///./src/apidata.db'


if (settings.debugging):
    engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})
else:
    engine = create_engine(POSTGRES_DATABASE_URL)
    

SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_session():
    db = SessionLocal()
    return db
