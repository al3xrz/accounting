from pydantic import BaseModel


class STransportCompanyCreate(BaseModel):
    name: str


class STransportCompany(STransportCompanyCreate):
    id: int

