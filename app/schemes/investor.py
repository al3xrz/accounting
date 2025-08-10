from pydantic import BaseModel


class SInvestorCreate(BaseModel):
    name: str


class SInvestor(SInvestorCreate):
    id: int
