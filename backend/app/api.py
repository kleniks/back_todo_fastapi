from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="TodoApp", version='1.0.0')

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/todo", tags=["todos"], response_model=List[schemas.Todo])
async def get_todos(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    db_todo = crud.get_todos(db, skip, limit)
    return db_todo
    


@app.post("/todo", tags=["todos"], response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = crud.create_todo(db, todo)
    return 


# @app.put("/todo/{id}", tags=["todos"],response_model=schemas.Todo)
# async def update_todo(db: Session = Depends(get_db), id: int):
#    crud.create_todo
#    return crud.get_todos(db)


@app.delete("/todo/{id}", tags=["todos"], response_model=schemas.Todo)
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    crud.delete(db, todo_id)