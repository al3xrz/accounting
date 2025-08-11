from pydantic import BaseModel


class SStatusCreate(BaseModel):
    code: int
    explanation: str


class SStatus(SStatusCreate):
    id: int
