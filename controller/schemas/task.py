from typing import Optional
from .base import DateTime, CamelModel, ORMModel


class TaskBase(CamelModel):
    title: str
    description: str
    updated_at: Optional[DateTime] = None


# Properties to receive on item creation
class TaskCreate(TaskBase):
    pass


# Properties to receive on item update
class TaskUpdate(TaskBase):
    id: int


class TaskInDBBase(TaskBase):
    pass


# Properties to return to client
class Task(TaskInDBBase, ORMModel):
    id: int
    created_at: DateTime
