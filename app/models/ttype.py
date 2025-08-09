from sqlalchemy import Integer, Column, String
from .base import Base

class TransactionType(Base):
    __tablename__ = "transaction_type"
    __table_args__ = {
        "comment" : "Тип сделки"
    }

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Уникальный ID")
    name = Column(String, unique=True, nullable=False, comment="Тип сделки")

