from .base import BaseDAO
from models.expense import Expense

class ExpenseDAO(BaseDAO):
    model = Expense
    