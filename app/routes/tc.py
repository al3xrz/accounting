from fastapi import APIRouter,  HTTPException
from schemes.tc import STransportCompany, STransportCompanyCreate
from typing import List
from dao.tc import TCDAO
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/tc",
    tags=["Транспортные компании"]
)


@router.get("/", response_model=List[STransportCompany])
def all():
    db_tc = TCDAO.find_all()
    return db_tc


@router.get("/{tc_id}", response_model=STransportCompany)
def get_by_id(tc_id: int):
    db_tc = TCDAO.find_by_id(model_id=tc_id)
    if db_tc:
        return db_tc
    else:
        raise HTTPException(400, "Транспортная компания не найдена")


@router.post("/")
def create(tc: STransportCompanyCreate):
    try:
        TCDAO.add(name=tc.name)
        return {"detail": "Транспортная компания успешно зарегистрирована"}
    except IntegrityError:
        raise HTTPException(409, "Транспортная компания уже зарегистрирована")
