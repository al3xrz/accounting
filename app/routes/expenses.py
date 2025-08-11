from fastapi import APIRouter, HTTPException
from dao.expense import ExpenseDAO
from sqlalchemy.exc import IntegrityError
from schemes.expense import SExpense, SExpenseCreate
from typing import List

router = APIRouter(prefix="/expenses", tags=["Расходы"])


@router.get("/", response_model=List[SExpense])
def all():
    db_expenses = ExpenseDAO.find_all()
    return db_expenses


@router.get("${expense_id}", response_model=SExpense)
def get_by_id(expense_id: int):
    db_expense = ExpenseDAO.find_by_id(model_id=expense_id)
    if db_expense:
        return db_expense
    else:
        raise HTTPException(400, "Тип расходов не найден")


@router.post("/")
def create(expense: SExpenseCreate):
    try:
        ExpenseDAO.add(type=expense.type)
        return {"detail" : "Тип расходов успешно добавлен"}
    except IntegrityError:
        raise HTTPException(409, "Тип расходов уже существует")
