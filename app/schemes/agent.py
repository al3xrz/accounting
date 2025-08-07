from pydantic import BaseModel


class SAgentCreate(BaseModel):
    name: str


class SAgent(SAgentCreate):
    id: int
