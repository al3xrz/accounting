from fastapi import APIRouter,  HTTPException
from schemes.investor import SInvestor, SInvestorCreate
from typing import List
from dao.investor import InvestorDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/investor",
    tags=["Инвестор"]
)


@router.get("/", response_model=List[SInvestor])
def all():
    db_investors = InvestorDAO.find_all()
    return db_investors


@router.get("/{investor_id}", response_model=SInvestor)
def get_by_id(investor_id: int):
    db_investor = InvestorDAO.find_by_id(model_id=investor_id)
    if db_investor:
        return db_investor
    else:
        raise HTTPException(400, "Инвестор с заданным ID не найден")


@router.post("/")
def create(investor: SInvestorCreate):
    try:
        InvestorDAO.add(name=investor.name)
        return {"detail": "Инвестор успешно создан"}
    except IntegrityError:
        raise HTTPException(409, "Инвестор уже существует")
