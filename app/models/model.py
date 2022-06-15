from sqlalchemy import Column, Integer, String, Boolean, Table
from app.db.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    name = Column(String)
