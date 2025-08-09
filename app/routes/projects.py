from fastapi import APIRouter
from sqlalchemy.orm import selectinload
from schemes.projects import SProjectCreate
from dao.project import ProjectDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/projects",
    tags=["Проекты"]
)


@router.get("/")
def all():
    db_projects = ProjectDAO.find_all()
    return db_projects


@router.get("/populated")
def all_populated():
    populated_projects = ProjectDAO.all_populated()
    return populated_projects


@router.post("/")
def create(project: SProjectCreate):
    ProjectDAO.create_project_safe(project_data=project)
    return {"message": "Проект успешно создан"}
