# schemas.py
from pydantic import BaseModel
from datetime import datetime

class ScheduledPostBase(BaseModel):
    content: str
    platform: str
    scheduled_time: datetime

class ScheduledPostCreate(ScheduledPostBase):
    pass

class ScheduledPostUpdate(BaseModel):
    content: str = None
    scheduled_time: datetime = None

class ScheduledPostResponse(ScheduledPostBase):
    id: int
    status: str

    class Config:
        orm_mode = True
