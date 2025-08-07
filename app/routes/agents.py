from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from schemes.agent import SAgentCreate, SAgent
from models.agent import Agent
from .dependensy import get_db


router = APIRouter(
    prefix="/agents",
    tags=["Агенты"]
)


@router.get("/", response_model=List[SAgent])
def all(db: Session = Depends(get_db)):
    db_agents = db.query(Agent).all()
    return db_agents


@router.get("/{agent_id}", response_model=SAgent)
def get_by_id(agent_id: int, db=Depends(get_db)):
    db_agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if db_agent:
        return db_agent
    else:
        raise HTTPException(400, "Агент не найден")


@router.post("/")
def create(agent: SAgentCreate, db: Session = Depends(get_db)):
    db_agent = Agent(name=agent.name)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return {"message": "Агент успешно создан"}
