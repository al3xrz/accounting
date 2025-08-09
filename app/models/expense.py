from .base import Base
from sqlalchemy import Integer, Column, String

class Expense(Base):
    __tablename__ = "expense"
    __table_args__ = {
        "comment" : "Расходы"
    }

    id = Column(Integer, autoincrement=True, primary_key=True, comment="Уникальный ID")
    type = Column(String, nullable=False, unique=True, comment="Тип расходов")
    