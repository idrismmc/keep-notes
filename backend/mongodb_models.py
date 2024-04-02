from typing import Optional
from pydantic import BaseModel

class Note_Item(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool