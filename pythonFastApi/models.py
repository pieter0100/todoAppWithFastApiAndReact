from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TodoThing(Base):
    __tablename__ = "todos" # Nazwa tabeli w bazie danych

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    isDone = Column(Boolean)

class TodoCreate(BaseModel):
    text: str
    isDone: bool

class TodoResponse(BaseModel):
    id: int
    text: str
    isDone: bool

