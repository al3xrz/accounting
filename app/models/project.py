from sqlalchemy import ForeignKey, Column, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Project(Base):
    __tablename__ = "projects"

    client_id = Column(Integer, ForeignKey("clients.id"), primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"), primary_key=True)

    joined_at = Column(DateTime, default=datetime.now)
    
    agent = relationship("Agent", back_populates="client_projects")
    client = relationship("Client", back_populates="agent_projects")

    