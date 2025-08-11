from fastapi import APIRouter, HTTPException
from typing import List
from dao.status import ContractStatusDAO
from schemes.status import SStatus, SStatusCreate
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/statuses", tags=["Статус контракта"])


@router.get("/", response_model=List[SStatus])
def all():
    db_statuses = ContractStatusDAO.find_all()
    return db_statuses


@router.get("/{status_id}", response_model=SStatus)
def get_by_id(status_id: int):
    db_status = ContractStatusDAO.find_by_id(model_id=status_id)
    if db_status:
        return db_status
    else:
        raise HTTPException(400, "Статус не найден")


@router.post("/")
def create(status: SStatusCreate):
    try:
        ContractStatusDAO.add(
            code=status.code,
            explanation=status.explanation
        )
        return {"detail" : "Статус успешно добавлен"}
    except IntegrityError:
        raise HTTPException(409, "Статус уже зарегистрирован")

