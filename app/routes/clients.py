from fastapi import APIRouter,  HTTPException
from schemes.client import SClientCreate, SClient
from typing import List
from dao.client import ClientDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/clients",
    tags=["Заказчики"]
)


@router.get("/", response_model=List[SClient])
def all():
    db_clients = ClientDAO.find_all()
    return db_clients


@router.get("/{client_id}", response_model=SClient)
def get_by_id(client_id: int):
    db_client = ClientDAO.find_by_id(model_id=client_id)
    if db_client:
        return db_client
    else:
        raise HTTPException(400, "Заказчик не найден")


@router.post("/")
def create(client: SClientCreate):
    try:
        ClientDAO.add(name=client.name)
        return {"detail": "Новый заказчик успешно создан"}
    except IntegrityError:
        print("Заказчик уже существует")
        raise HTTPException(409, "Заказчик уже существует")
