from pydantic import BaseModel


class SStatusCreate(BaseModel):
    code: int
    explanation: int


class SStatus(SStatusCreate):
    id: int
