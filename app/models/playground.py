from sqlalchemy import Integer, Column, String
from .base import Base

class Playground(Base):
    __tablename__ = "playground"
    __table_args__ = {
        "comment" : "Площадка"
    }

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Уникальный ID")
    name = Column(String, nullable=False, unique=True, comment="Наименование площадки")
