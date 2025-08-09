from sqlalchemy import ForeignKey, Column, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Project(Base):
    __tablename__ = "projects"
    __table_args__ = {
        "comment" : "Проекты"
    }

    id = Column(Integer, primary_key=True, autoincrement=True)

    client_id = Column(Integer, ForeignKey("clients.id"))
    agent_id = Column(Integer, ForeignKey("agents.id"))

    joined_at = Column(DateTime, default=datetime.now)

    agent = relationship("Agent", back_populates="client_projects")
    client = relationship("Client", back_populates="agent_projects")
