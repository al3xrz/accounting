from .base import BaseDAO
from models.investor import Investor

class InvestorDAO(BaseDAO):
    model = Investor
    