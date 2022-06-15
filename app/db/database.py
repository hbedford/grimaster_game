from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import os

BASE_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', '..')

SQLALCHEMY_DATABASE_URL = f'sqlite:///{os.path.join(BASE_DIRECTORY, "app_event2.db")}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, **{
    'connect_args': {
        'check_same_thread': False
    },
    'poolclass': StaticPool
})

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_session():
    session = SessionLocal()
    return session
