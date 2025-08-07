from pydantic import BaseModel


class SClientCreate(BaseModel):
    name: str


class SClient(SClientCreate):
    id: int
