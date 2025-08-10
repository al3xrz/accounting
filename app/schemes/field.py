from pydantic import BaseModel


class SFieldCreate(BaseModel):
    name: str


class SField(SFieldCreate):
    id: int
