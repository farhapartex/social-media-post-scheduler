# models.py
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class ScheduledPost(Base):
    __tablename__ = "scheduled_posts"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    platform = Column(String, nullable=False)  # e.g., Twitter, Facebook
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String, default="scheduled")  # scheduled, posted, cancelled
