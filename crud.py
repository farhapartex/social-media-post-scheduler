# crud.py
from sqlalchemy.orm import Session
from models import ScheduledPost
from schemas import ScheduledPostCreate, ScheduledPostUpdate

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ScheduledPost).offset(skip).limit(limit).all()

def get_post(db: Session, post_id: int):
    return db.query(ScheduledPost).filter(ScheduledPost.id == post_id).first()

def create_post(db: Session, post: ScheduledPostCreate):
    db_post = ScheduledPost(
        content=post.content,
        platform=post.platform,
        scheduled_time=post.scheduled_time
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post: ScheduledPostUpdate):
    db_post = get_post(db, post_id)
    if db_post:
        if post.content:
            db_post.content = post.content
        if post.scheduled_time:
            db_post.scheduled_time = post.scheduled_time
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post
