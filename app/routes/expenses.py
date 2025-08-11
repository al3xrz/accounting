from fastapi import APIRouter, HTTPException
from dao.expense import ExpenseDAO
from sqlalchemy.exc import IntegrityError
from schemes.expense import SExpense, SExpenseCreate


router = APIRouter(prefix="/expenses", tags=["Расходы"])


@router.get("/")
def all():
    db_expenses = ExpenseDAO.find_all()
    return db_expenses


@router.get("${expense_id}")
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
        
    except IntegrityError:
     pass        
