from .base import Base
from sqlalchemy import Column, Integer, String


class Comment(Base):

    __tablename__ = "comments"
    __table_args__ = {
        "comment" : "Комментарии к проекту"
    }

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Уникальный id")
    text = Column(String, comment="Текст комментария", unique=True)