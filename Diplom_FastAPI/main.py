from typing import Annotated
from fastapi import FastAPI, HTTPException, Request, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from backend.db import SessionLocal
from schemas import Post
from models.post import PostModel
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def read_posts(request: Request, db: Annotated[Session, Depends(get_db)]):
    posts = db.scalars(select(PostModel)).all()
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts})


@app.post("/posts/", response_model=Post)
async def create_post(post: Post, db: Annotated[Session, Depends(get_db)]):
    new_post = insert(PostModel).values(title=post.title,
                                        rezume=post.rezume,
                                        info=post.info,
                                        created_at=datetime.now())
    db.execute(new_post)
    db.commit()
    db_post = db.query(PostModel).filter(PostModel.title == post.title).first()
    return db_post


@app.delete("/posts/{post_id}", response_model=Post)
async def delete_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    post_to_delete = db.scalar(PostModel).where(PostModel.id == post_id)
    if post_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
    db.delete(post_to_delete)
    db.commit()
    return {'transaction': 'Post delete is successful'}
