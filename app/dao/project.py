from .base import BaseDAO
from models import Project
from sqlalchemy.orm import selectinload
from database import SessionLocal
from models.client import Client
from models.agent import Agent
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from .client import ClientDAO
from .agent import AgentDAO


class ProjectDAO(BaseDAO):
    model = Project

    @staticmethod
    def all_populated():
        with SessionLocal() as session:
            populated_projects = session.query(Project)\
                .options(
                selectinload(Project.agent),
                selectinload(Project.client)
            ).all()
            return populated_projects

    @staticmethod
    def create_project_safe(project_data):
        try:
            # Явная проверка перед вставкой
            if not ClientDAO.find_by_id(project_data.client_id):
                raise ValueError("Заказчик не существует")
            if not AgentDAO.find_by_id(project_data.agent_id):
                raise ValueError("Поставщик не существует")
            ProjectDAO.add(
                client_id=project_data.client_id,
                agent_id=project_data.agent_id
            )

        except (IntegrityError, ValueError):
            raise HTTPException(
                409, "Неправильные ID поставщика или заказчика")
