from fastapi import APIRouter, Depends
from sqlalchemy.orm import selectinload
from models import Project
from .dependensy import get_db
from schemes.projects import SProjectCreate 


router = APIRouter(
    prefix="/projects",
    tags = ["Проекты"]
)

@router.get("/")
def all(db=Depends(get_db)):
    db_projects = db.query(Project).all()
    return db_projects

@router.get("/poulated")
def all_populated(db=Depends(get_db)):
    populated_projects = db.query(Project)\
    .options(
        selectinload(Project.agent),
        selectinload(Project.client)
    ).all()
    return populated_projects

@router.post("/")
def create(project: SProjectCreate, db=Depends(get_db)):
    db_project = Project(client_id=project.client_id, agent_id=project.agent_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return {"message" : "Проект успешно создан"}