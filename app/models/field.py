from .base import Base
from sqlalchemy import Integer, Column, String

class Field(Base):
    __tablename__ = "field"
    __table_args__ = {
        "comment" : "Сфера деятельности"
    }

    id = Column(Integer, autoincrement=True, primary_key=True, comment="Уникальный id")
    name = Column(String(255), unique=True, nullable=False, comment="Наименование сферы детельности")


