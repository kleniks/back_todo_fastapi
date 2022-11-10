from sqlalchemy.orm import Session
from sqlalchemy import delete

from . import models, schemas


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, id: int):
    delete_todo = db.query(models.Todo).filter(models.Todo.id==id).delete()
    db.commit()


