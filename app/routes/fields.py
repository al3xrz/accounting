from fastapi import APIRouter,  HTTPException
from schemes.field import SField, SFieldCreate
from typing import List
from dao.field import FieldDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/fields",
    tags=["Поле деятельности"]
)


@router.get("/", response_model=List[SField])
def all():
    db_fields = FieldDAO.find_all()
    return db_fields


@router.get("/{field_id}", response_model=SField)
def get_by_id(field_id: int):
    db_fields = FieldDAO.find_by_id(model_id=field_id)
    if db_fields:
        return db_fields
    else:
        raise HTTPException(400, "Поле деятельности с заданным ID не найдено")


@router.post("/")
def create(field: SFieldCreate):
    try:
        FieldDAO.add(name=field.name)
        return {"detail": "Поле деятельности успешно создано"}
    except IntegrityError:
        raise HTTPException(409, "Поле деятельности уже существует")
