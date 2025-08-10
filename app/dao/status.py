from .base import BaseDAO
from models.status import ContractStatus

class ContractStatusDAO(BaseDAO):
    model = ContractStatus
    