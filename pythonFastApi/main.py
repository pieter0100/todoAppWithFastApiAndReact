from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends

import models
from database import engine, SessionLocal
from models import TodoCreate
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# CORS
origins = [
    "http://localhost:3000",  # Domyślny port dla Create React App
    "http://localhost:5173",  # Domyślny port dla Vite (bardzo polecam zamiast CRA!)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    # Zezwól na zapytania z tych adresów
    allow_credentials=True,
    allow_methods=["*"],      # Zezwól na wszystkie metody HTTP (GET, POST, etc.)
    allow_headers=["*"],      # Zezwól na wszystkie nagłówki
)

items = ["test"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items", response_model=list[models.TodoResponse])
def get_todos(db: Session  = Depends(get_db)):
    todos = db.query(models.TodoThing).all()

    return todos

@app.post("/items")
def create_todo(todo: TodoCreate, db: Session  = Depends(get_db)):
    new_todo = models.TodoThing(text=todo.text, isDone=todo.isDone)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

@app.delete("/items/{item_id}")
def delete_todo(item_id: int, db: Session = Depends(get_db)):
    todo_to_delete = db.query(models.TodoThing).filter(models.TodoThing.id == item_id).first()

    if todo_to_delete is None:
        raise HTTPException(status_code=404, detail="Zadanie o podanym ID nie istnieje")

    db.delete(todo_to_delete)
    db.commit()

    return {"message": "Zadanie zostało pomyślnie usunięte"}


@app.put("/items/{item_id}", response_model=models.TodoResponse)
def update_todo(item_id: int, todo_update: models.TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoThing).filter(models.TodoThing.id == item_id).first()

    if db_todo is None:
        raise HTTPException(status_code=404, detail="Zadanie nie istnieje")

    db_todo.text = todo_update.text
    db_todo.isDone = todo_update.isDone

    db.commit()

    db.refresh(db_todo)

    return db_todo

