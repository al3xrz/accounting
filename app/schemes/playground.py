from pydantic import BaseModel


class SPlaygroundCreate(BaseModel):
    name: str


class SPlayground(SPlaygroundCreate):
    id: int
