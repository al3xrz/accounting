from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = "clients"
    __table_args__ = {
        "comment" : "Организация заказчик"
    }

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, comment="Уникальный ID")
    name = Column(String, unique=True, comment="Наименование")
    agent_projects = relationship("Project", back_populates="client")
    