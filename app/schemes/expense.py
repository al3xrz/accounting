from pydantic import BaseModel


class SExpenseCreate(BaseModel):
    type: str


class SExpense(SExpenseCreate):
    id: int
