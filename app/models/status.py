from .base import Base
from sqlalchemy import Column, Integer, String

class ContractStatus(Base):
    __tablename__ = "contract_status"
    __table_args__ = {
        "comment" : "Справочник статусов договоров"
    }

    id = Column(Integer, autoincrement=True, primary_key=True, comment="Уникальный идентификатор")
    code = Column(Integer, unique=True, comment="Числовой код статуса", nullable=False)
    explanations = Column(String(255), unique=True, comment="Текстовое описание статуса", nullable=False)