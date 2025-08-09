from .base import Base
from sqlalchemy import Integer, Column, String

class TC(Base):
    __tablename__ = "tc"
    __table_args__ = {
        "comment" : "Транспортная компания"
    }

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Уникальный ID")
    name = Column(String(255), unique=True, nullable=False)
