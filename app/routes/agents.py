from fastapi import APIRouter, HTTPException
from typing import List
from schemes.agent import SAgentCreate, SAgent
from dao.agent import AgentDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/agents",
    tags=["Агенты"]
)


@router.get("/", response_model=List[SAgent])
def all():
    db_agents = AgentDAO.find_all()
    return db_agents


@router.get("/{agent_id}", response_model=SAgent)
def get_by_id(agent_id: int):
    db_agent = AgentDAO.find_by_id(model_id=agent_id)
    if db_agent:
        return db_agent
    else:
        raise HTTPException(400, "Агент не найден")


@router.post("/")
def create(agent: SAgentCreate):
    try:
        AgentDAO.add(name=agent.name)
        return {"detail": "Агент успешно создан"}
    except IntegrityError:
        print("Организация с таким именем уже существует")
        raise HTTPException(409, "Организация уже существует")