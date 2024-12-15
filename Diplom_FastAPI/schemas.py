from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    id: int
    title: str
    rezume: str
    info: str
    created_at: datetime = None


