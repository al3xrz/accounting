from fastapi import APIRouter, Depends, HTTPException
from schemes.client import SClientCreate, SClient
from .dependensy import get_db
from models.client import Client
from typing import List

router = APIRouter(
    prefix="/clients",
    tags=["Клиенты"]
)


@router.get("/", response_model=List[SClient])
def all(db=Depends(get_db)):
    db_clients = db.query(Client).all()
    return db_clients   


@router.get("/{client_id}", response_model=SClient)
def get_by_id(client_id: int, db=Depends(get_db)):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        return db_client
    else:
        raise HTTPException(400, "Клиент не найден")



@router.post("/")
def create(client: SClientCreate, db=Depends(get_db)):
    db_client = Client(name=client.name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"message": "Клиент успешно создан"}
