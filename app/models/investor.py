from .base import Base
from sqlalchemy import Column, Integer, String

class Investor(Base):
    __tablename__ = "investor"
    __table_args__ = {
        "comment" : "Справочник инвесторов"
    }

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Уникальный id")
    name = Column(String(255), unique=True, nullable=False, comment="Инвестор")