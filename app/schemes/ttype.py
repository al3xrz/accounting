from pydantic import BaseModel


class STransactionTypeCreate(BaseModel):
    name: str


class STransactionType(STransactionTypeCreate):
    id: int
