# routers/posts.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ScheduledPostCreate, ScheduledPostUpdate, ScheduledPostResponse
import crud

router = APIRouter()

@router.post("/", response_model=ScheduledPostResponse)
def create_scheduled_post(post: ScheduledPostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

@router.get("/", response_model=list[ScheduledPostResponse])
def get_scheduled_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip, limit)

@router.put("/{post_id}", response_model=ScheduledPostResponse)
def update_scheduled_post(post_id: int, post: ScheduledPostUpdate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db, post_id, post)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.delete("/{post_id}")
def delete_scheduled_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.delete_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
