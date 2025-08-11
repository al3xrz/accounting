from fastapi import APIRouter, HTTPException
from dao.comment import CommentDAO
from typing import List
from schemes.comment import SComment, SCommentCreate
from sqlalchemy.exc import IntegrityError



router = APIRouter(
    prefix="/comments",
    tags = ["Комментарии"]
)

@router.get("/", response_model=List[SComment])
def all():
    db_all = CommentDAO.find_all()
    return db_all

@router.get("/{comment_id}", response_model=SComment)
def get_by_id(comment_id: int):
    db_comment = CommentDAO.find_by_id(model_id = comment_id)
    if db_comment:
        return db_comment
    else:
        raise HTTPException(400, "Комментарий не найден")
    
@router.post("/")
def create(comment: SCommentCreate):
    try:
        CommentDAO.add(text = comment.text)
        return {"detail" : "Комментарий успешно создан"}
    except IntegrityError:
        raise HTTPException(409, "Комментарий уже существует")