from fastapi import APIRouter,  HTTPException
from schemes.playground import SPlayground, SPlaygroundCreate
from typing import List
from dao.playground import PlaygroundDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/playgrounds",
    tags=["Площадки"]
)


@router.get("/", response_model=List[SPlayground])
def all():
    db_playgrounds = PlaygroundDAO.find_all()
    return db_playgrounds


@router.get("/{client_id}", response_model=SPlayground)
def get_by_id(client_id: int):
    db_playground = PlaygroundDAO.find_by_id(model_id=client_id)
    if db_playground:
        return db_playground
    else:
        raise HTTPException(400, "Площадка не найдена")


@router.post("/")
def create(playground: SPlaygroundCreate):
    try:
        PlaygroundDAO.add(name=playground.name)
        return {"detail": "Площадка успешно зарегистрирована"}
    except IntegrityError:
        raise HTTPException(409, "Площадка уже зарегистрирована")
