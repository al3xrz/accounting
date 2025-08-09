from .base import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

class Agent(Base):
    __tablename__ = "agents"
    __table_args = {
        "comment" : "Организация исполнитель"
    }

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Уникальный ID")
    name = Column(String, unique=True, comment="Наименование организации")
    client_projects = relationship("Project", back_populates="agent")
    