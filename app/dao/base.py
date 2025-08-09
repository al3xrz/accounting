from database import SessionLocal
from sqlalchemy import select, insert, delete
from typing import TypeVar, Type, Dict, Any, Optional
from sqlalchemy.orm import DeclarativeBase

T = TypeVar('T', bound='DeclarativeBase')  # Для SQLAlchemy моделей


class BaseDAO:

    model = None

    @classmethod
    def update_by_id(cls: Type[Any], model_id, data):
        with SessionLocal() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = session.execute(query)
            db_item = result.scalars().first()
            for key, value in data.items():
                setattr(db_item, key, value)
            session.commit()
            session.refresh(db_item)

    @classmethod
    def remove_by_id(cls: Type[Any], model_id: int):
        with SessionLocal() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            result = session.execute(query)
            session.commit()
            return result.rowcount

    @classmethod
    def find_by_id(cls: Type[Any], model_id: int):
        with SessionLocal() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    def find_one_or_none(cls: Type[Any], **filter_by):
        with SessionLocal() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    def find_all(cls: Type[Any], **filter_by):
        with SessionLocal() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = session.execute(query)

            return result.scalars().all()

    @classmethod
    def add(cls: Type[Any], **data):
        with SessionLocal() as session:
            query = insert(cls.model).values(**data)
            print(query)
            session.execute(query)
            session.commit()
