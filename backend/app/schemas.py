from pydantic import BaseModel


class TodoBase(BaseModel):
    record: str
    priority: bool | None = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True