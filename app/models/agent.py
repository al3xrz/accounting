from .base import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    client_projects = relationship("Project", back_populates="agent")
    