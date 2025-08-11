from fastapi import APIRouter,  HTTPException
from schemes.ttype import STransactionType, STransactionTypeCreate
from typing import List
from dao.ttype import TransactionTypeDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/ttype",
    tags=["Тип сделки"]
)


@router.get("/", response_model=List[STransactionType])
def all():
    db_ttype = TransactionTypeDAO.find_all()
    return db_ttype


@router.get("/{ttype_id}", response_model=STransactionType)
def get_by_id(ttype_id: int):
    db_ttype = TransactionTypeDAO.find_by_id(model_id=ttype_id)
    if db_ttype:
        return db_ttype
    else:
        raise HTTPException(400, "Тип сделки не найден")


@router.post("/")
def create(ttype: STransactionTypeCreate):
    try:
        TransactionTypeDAO.add(name=ttype.name)
        return {"detail": "Тип сделки успешно зарегистрирован"}
    except IntegrityError:
        raise HTTPException(409, "Тип сделки уже зарегистрирован")
