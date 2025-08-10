from .base import BaseDAO
from models.ttype import TransactionType

class TransactionTypeDAO(BaseDAO):
    model = TransactionType