from models.comment import Comment

from .base import BaseDAO

class CommentDAO(BaseDAO):
    model = Comment

