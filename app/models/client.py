from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    agent_projects = relationship("Project", back_populates="client")
    