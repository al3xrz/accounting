from pydantic import BaseModel


class SCommentCreate(BaseModel):
    text: str


class SComment(SCommentCreate):
    id: int
